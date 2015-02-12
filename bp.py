from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
#from pybrain.tools.customxml import NetworkWriter, NetworkReader
from time import sleep    
import pickle
global net,ds,trainer
net = None
ds = None
trainer = None


def init():
    global  net,ds,trainer
    net = buildNetwork(2,50,1)
    ds = SupervisedDataSet(2,1)
'''
def update_net(fname=None):
    global net
    #if not fname:
    #    fname = raw_input("fname: ")
    #f = file(fname)
    #tmp = pickle.load(f)
    #f.close()
    #NetworkWriter(tmp,'network233').writeToFile(net,'network233')
    a = NetworkReader('network233','nettmptmptmp')
    b = a.readFrom('network233')
    net = b
    net.sortModules()
'''
def mkds():
    global ds
    import pickle
    f = file('data.data','rb')
    a = pickle.load(f)
    for i in a:
        ds.addSample([i[0],i[1]],[i[2]])
    f.close()
    print 'load',len(ds)
def train(n = 100):
    global  net,ds,trainer
    trainer = BackpropTrainer(net, ds)
    trainer.train()
    for i in xrange(n):
        j = trainer.train()
        print n-i,'left','err:',j

def trainSave(n=100,logName='data.log',netName='net'):
    global net,ds,trainer
    if not trainer:
        trainer = BackpropTrainer(net, ds)
    filelog = file(logName,'a')
    for i in xrange(n):
        j = trainer.train()
        print n-i,'left err',j
        if i & 0x3 == 0:
            filelog.write("%d,%f\n"%(i,j))
            filelog.flush()
            print 'logged'
            if i & 0xff == 0:
                filenet = file("%s%d"%(netName,i),'w')
                pickle.dump(trainer.module,filenet)
                filenet.close()
                print 'dump'

def set_learning_rate(rate=0.0001,m=0):
    global trainer
    trainer.descent.alpha = rate
    trainer.descent.momentum = m