import argparse
import os
import shutil
import time
os.environ["CUDA_VISIBLE_DEVICES"] = "7"
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim
import torch.utils.data
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import vgg
#from dataloader import BboxDataset, ClassDataset, AllDataset
from dataloader import AllDataset
#from loss import BboxLoss
#print(vgg.__dict__)
model_names = sorted(name for name in vgg.__dict__
    if name.islower() and not name.startswith("__")
                     and name.startswith("vgg")
                     and callable(vgg.__dict__[name]))
print('model_names:', model_names)


parser = argparse.ArgumentParser(description='PyTorch ImageNet Training')
parser.add_argument('--start-epoch', default=0, type=int, metavar='N', help='manual epoch number (useful on restarts)')
parser.add_argument('--lr', '--learning-rate', default=1e-6, type=float, metavar='LR', help='initial learning rate')
parser.add_argument('--resume', default='', type=str, metavar='PATH', help='path to latest checkpoint (default: none)')
parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true', help='evaluate model on validation set')
parser.add_argument('--pretrained', dest='pretrained', action='store_true', help='use pre-trained model')
parser.add_argument('--save-dir', dest='save_dir', help='The directory used to save the trained models', default='save_temp', type=str)


best_prec1 = 0
workers = 4
epochs = 100
batch_size = 8
momentum = 0.9
weight_decay = 5e-4
#设定用于并行化CPU操作的OpenMP线程数
torch.set_num_threads(10)

print_freq = 20

def main():
    global args, best_prec1
    args = parser.parse_args()
    print('args:', args, type(args))
    # Check the save_dir exists or not
    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    model = vgg.__dict__['vgg11']()

    model.features = torch.nn.DataParallel(model.features)
    model.cuda()

    # optionally resume from a checkpoint
    if args.resume:
        if os.path.isfile(args.resume):
            print("=> loading checkpoint '{}'".format(args.resume))
            checkpoint = torch.load(args.resume)
            args.start_epoch = checkpoint['epoch']
            best_prec1 = checkpoint['best_prec1']
            model.load_state_dict(checkpoint['state_dict'])
            print("=> loaded checkpoint '{}' (epoch {})"
                  .format(args.evaluate, checkpoint['epoch']))
        else:
            print("=> no checkpoint found at '{}'".format(args.resume))

    cudnn.benchmark = True

    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    #train_loader = torch.utils.data.DataLoader(AllDataset(label_file='./train.txt', root_dir='/alps-security-storage/zoloz/yufei.gyf/boundary/src_img/'), batch_size=batch_size, shuffle=True, num_workers=workers, pin_memory=True)
    train_loader = torch.utils.data.DataLoader(AllDataset(label_file='./train5.txt', root_dir='/alps-security-storage/zoloz/yufei.gyf/boundary/src_img/'), batch_size=batch_size, shuffle=True, num_workers=workers, pin_memory=True)

    #val_loader = torch.utils.data.DataLoader(AllDataset(label_file='./test.txt', root_dir='/alps-security-storage/zoloz/yufei.gyf/boundary/src_img/'), batch_size=batch_size, shuffle=True, num_workers=workers, pin_memory=True)
    val_loader = torch.utils.data.DataLoader(AllDataset(label_file='./test5.txt', root_dir='/alps-security-storage/zoloz/yufei.gyf/boundary/src_img/'), batch_size=batch_size, shuffle=True, num_workers=workers, pin_memory=True)

    # define loss function (criterion) and pptimizer
    criterion1 = nn.CrossEntropyLoss().cuda()
    #criterion = BboxLoss()
    criterion0 = nn.MSELoss().cuda()
    criterion  = [criterion0, criterion1]

    optimizer = torch.optim.SGD(model.parameters(), args.lr, momentum=momentum, weight_decay=weight_decay)

    if args.evaluate:
        validate(val_loader, model, criterion)
        return

    for epoch in range(args.start_epoch, epochs):
        adjust_learning_rate(optimizer, epoch)
        # train for one epoch
        train(train_loader, model, criterion, optimizer, epoch)
        # evaluate on validation set
        prec1 = validate(val_loader, model, criterion)

        # remember best prec@1 and save checkpoint
        is_best = prec1 > best_prec1
        best_prec1 = max(prec1, best_prec1)
        save_checkpoint({
            'epoch': epoch + 1,
            'state_dict': model.state_dict(),
            #'state_dict': model,
            'best_prec1': best_prec1,
        }, is_best, filename=os.path.join(args.save_dir, 'checkpoint_{}.tar'.format(epoch)))


def train(train_loader, model, criterion, optimizer, epoch):
    batch_time = AverageMeter()
    data_time = AverageMeter()
    losses = AverageMeter()
    top1 = AverageMeter()

    # switch to train mode
    model.train()

    end = time.time()
    for i, (input, target) in enumerate(train_loader):

        # measure data loading time
        data_time.update(time.time() - end)

        target = target.cuda(async=True)
        input_var = torch.autograd.Variable(input).cuda()
        target_var = torch.autograd.Variable(target)

        # compute output
        output = model(input_var)
        if 1:
            loss = criterion[0](output, target_var)
        else:
            loss0 = criterion[0](output[:,:8], target_var[:,:8])
            loss1 = criterion[1](output[:,-10:], target_var[:,-1].long())
            loss = 100*loss0

        #loss = criterion[1](output, target_var)

        # compute gradient and do SGD step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        output = output.float()
        loss = loss.float()
        # measure accuracy and record loss
        #prec1 = accuracy(output.data[:,-10:], target[:,-1])[0]
        #prec1 = accuracy(output.data, target)[0]
        prec1 = [0]
        losses.update(loss.data[0], input.size(0))
        top1.update(prec1[0], input.size(0))

        # measure elapsed time
        batch_time.update(time.time() - end)
        end = time.time()

        if i % print_freq == 0:
            print('Epoch: [{0}][{1}/{2}]\tTime {batch_time.val:.3f} ({batch_time.avg:.3f})\tData {data_time.val:.3f} ({data_time.avg:.3f})\tLoss {loss.val:.4f} ({loss.avg:.4f})\tPrec@1 {top1.val:.3f} ({top1.avg:.3f})'.format(epoch, i, len(train_loader), batch_time=batch_time, data_time=data_time, loss=losses, top1=top1))


def validate(val_loader, model, criterion):
    batch_time = AverageMeter()
    losses = AverageMeter()
    top1 = AverageMeter()

    # switch to evaluate mode
    model.eval()

    end = time.time()
    for i, (input, target) in enumerate(val_loader):
        target = target.cuda(async=True)
        input_var = torch.autograd.Variable(input, volatile=True).cuda()
        target_var = torch.autograd.Variable(target, volatile=True)

        # compute output
        output = model(input_var)
        if 1:
            loss = criterion[0](output, target_var)
        else:
            loss0 = criterion[0](output[:,:8], target_var[:,:8])
            loss1 = criterion[1](output[:,-10:], target_var[:,-1].long())
            loss = 100*loss0

        #loss = criterion[1](output, target_var)

        output = output.float()
        loss = loss.float()

        # measure accuracy and record loss
        #prec1 = accuracy(output.data[:,-10:], target[:,-1])[0]
        #prec1 = accuracy(output.data, target)[0]
        prec1 = [0]
        losses.update(loss.data[0], input.size(0))
        top1.update(prec1[0], input.size(0))

        # measure elapsed time
        batch_time.update(time.time() - end)
        end = time.time()

        if i % print_freq == 0:
            print('Test: [{0}/{1}]\tTime {batch_time.val:.3f} ({batch_time.avg:.3f})\tLoss {loss.val:.4f} ({loss.avg:.4f})\tPrec@1 {top1.val:.3f} ({top1.avg:.3f})'.format(i, len(val_loader), batch_time=batch_time, loss=losses, top1=top1))

    print(' * Prec@1 {top1.avg:.3f}'.format(top1=top1))

    return top1.avg

def save_checkpoint(state, is_best, filename='checkpoint.pth.tar'):
    torch.save(state, filename)

class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


def adjust_learning_rate(optimizer, epoch):
    """Sets the learning rate to the initial LR decayed by 2 every 30 epochs"""
    lr = args.lr * (0.3 ** (epoch // 1))
    for param_group in optimizer.param_groups:
        param_group['lr'] = lr


def accuracy(output, target, topk=(1,)):
    maxk = max(topk)
    batch_size = target.size(0)

    _, pred = output.topk(maxk, 1, True, True)
    pred = pred.t()
    correct = pred.eq(target.long().view(1, -1).expand_as(pred))

    res = []
    for k in topk:
        correct_k = correct[:k].view(-1).float().sum(0)
        res.append(correct_k.mul_(100.0 / batch_size))
    return res


if __name__ == '__main__':
    main()
