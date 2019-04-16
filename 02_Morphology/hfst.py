import hfst

ifs = hfst.HfstInputStream('chv.gen.hfst') # set up an input stream
transducer = ifs.read()                    # read the first transducer
transducer.invert()                        # invert the transducer
transducer.lookup('урамӑн')                # analyse a token