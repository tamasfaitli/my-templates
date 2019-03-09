#################################################################################################################
#  Author:      Tamas Faitli                                                                                    #
#  Date:        05/03/2019                                                                                      #
#  Name:        template_python.py                                                                              #
#  Description: This is a template module which can be                                                          #
#               used for initializing empty scripts                                                             #
#################################################################################################################

#################################################################################################################
#   HELP MESSAGE                                                                                                #
#################################################################################################################
HELP_MESSAGE = '''
'''
#################################################################################################################
#   IMPORTS                                                                                                     #
#################################################################################################################
import os
import sys
import time
import pbd
#import subprocess
#import re
#import unittest

#################################################################################################################
#   DEFAULT CONFIG                                                                                              #
#################################################################################################################
CONF_DEBUG              = False

#################################################################################################################
#   ARGUMENTS                                                                                                   #
#################################################################################################################
# input arguments
arguments_with_options  = sys.argv
arguments               = [arg[:arg.find(':')] if ':' in arg else arg for arg in arguments_with_options]
# arguments separated by functionality
arg_debug               = ['-debug','-d']
arg_help                = ['-help','-h','-?']
arg_temp                = ['-init']
# total supported arguments
arg_supported           = arg_debug + arg_help + arg_temp
# check whether all argument is supported or not
if any(arg not in arg_supported for arg in arguments):
    print 'Invalid argument! See supported arguments passing -help .'
    exit(1)
# check if any help argument is passed
if any(arg in arg_help for arg in arguments):
    print HELP_MESSAGE
    exit(0)
# check if any debug argument is passed
if any(arg in arg_debug for arg in arguments):
    print 'Debug mode is activated!'
    CONF_DEBUG          = True
    pbd.set_trace()

#################################################################################################################
#   PARAMETERS                                                                                                  #
#################################################################################################################
PAR_TEMP                = 'template_python.py'

#################################################################################################################
#   CLASS DEFINITIONS                                                                                           #
#################################################################################################################

#################################################################################################################
#   GLOBAL VARIABLES                                                                                            #
#################################################################################################################

#################################################################################################################
#   FUNCTION DEFINITIONS                                                                                        #
#################################################################################################################

#################################################################################################################
#   MAIN                                                                                                        #
#################################################################################################################
if __name__=="__main__":
    TIME_START  = time.time()
    # beginning of body of main
    pass # do stuff
    # end of body of main
    TIME_END    = time.time()
    # print execution time
    print("--- %s seconds ---" % (TIME_END - TIME_START))
    pass
#################################################################################################################
#   UNIT TESTS                                                                                                  #
#################################################################################################################