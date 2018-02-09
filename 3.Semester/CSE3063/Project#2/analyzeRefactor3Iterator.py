# encoding:utf8
import sys
import re
import os
import psutil # if this makes an error, you need to install the psutil package on your system
import time

maxmem = 0
def showMemTime(when='Resources'):
  global maxmem
  # memory and time measurement
  process = psutil.Process(os.getpid())
  mem = process.memory_info().rss / float(2 ** 20)
  maxmem = max(maxmem, mem)
  ts = process.cpu_times()
  sys.stderr.write("{when:<20}: {mb:4.0f} MB (max {maxmb:4.0f} MB), {user:4.1f} s user, {system:4.1f} s system\n".format(
    when=when, mb=mem, maxmb=maxmem, user=ts.user, system=ts.system))

class NGramCounter:
  def __init__(self, length):
    # initialize storage dictionary (datatype of {} is 'dict')
    self.ngrams = {}
    self.n = length

  def count(self, word):
    # make ngram (datatype of (,) is 'tuple')
    for idx in range(self.n-1,len(word)):
      self.registerNgram(word[idx-(self.n)+1:idx+1])

  def registerNgram(self, ngram):
    # increase count for this sequence by one
    if ngram not in self.ngrams:
      # if it was not yet in the dictionary
      self.ngrams[ngram] = 1
    else:
      # if it was already in the dictionary
      self.ngrams[ngram] += 1

  def display(self):
    showMemTime('begin display')

    # build list of all frequencies and ngrams
    ngram_freq = list(self.ngrams.items())
    showMemTime('after items')

    # sort that list by frequencies (i.e., second field), descending
    print("sorting ...")
    ngram_freq.sort(key = lambda x:x[1], reverse = True)
    showMemTime('after sorting')

    # iterate over the first five (or less) elements
    print("creating output ...")
    for ngram, occurred in ngram_freq[0:5]:
      try:
        # python 2
        ngram = unicode.encode(ngram, 'utf8')
      except:
        pass
      print("%sgram '%s' occured %d times" % (self.n, ngram, occurred))

# this is our main function
def main():
  # make sure the user gave us a file to read
  if len(sys.argv) != 2:
    print("need one argument! (file to read from)")
    sys.exit(-1)
  filename = sys.argv[1]

  showMemTime('begin') # let's observe where we use our memory and time

  print("reading from file "+filename)

  # initialize bigram counter
  bc = NGramCounter(2)
  tc = NGramCounter(3)

  f = open(filename, 'r')

  for line in f:
	  # read input file
	  inputdata = line
	  try:
	    # python 2: manual unicode
	    inputdata = unicode(inputdata, encoding='utf8')
	  except:
	    # python 3: unicode per default
	    pass

	  # split on all newlines and spaces
	  inputwords = re.split(r' |\n',inputdata)
	  
	  del inputdata

	  # remove empty strings
	  inputwords = list(filter(lambda x: x != '', inputwords))

	  # go through all words
	  for idx, token in enumerate(inputwords):
	    bc.count(token)
	    tc.count(token)

  showMemTime('after counting')
  print("bigrams:")
  bc.display()
  print("trigrams:")
  tc.display()

main()
showMemTime('at the end')
