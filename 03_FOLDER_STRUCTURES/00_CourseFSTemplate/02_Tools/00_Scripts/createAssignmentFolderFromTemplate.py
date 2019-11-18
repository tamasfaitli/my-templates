#################################################################################################################
#  Author:      Tamas Faitli                                                                                    #
#  Date:        23/09/2019                                                                                      #
#  Name:        createAssignmentFolderFromTemplate.py                                                           #
#  Description: This script build up a folder structure for a fresh new assignment                              #
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
import shutil
import re
#import unittest

#################################################################################################################
#   DEFAULT CONFIG                                                                                              #
#################################################################################################################
CONF_DEBUG              = False

#################################################################################################################
#   ARGUMENTS                                                                                                   #
#################################################################################################################
# input arguments
arguments_with_options  = sys.argv[1:] # passing on first element since it is always the path
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

#################################################################################################################
#   PARAMETERS                                                                                                  #
#################################################################################################################
PAR_PATH_OF_TEMPFOLDER          = "../../../../00_Templates/03_FOLDER_STRUCTURES"
PAR_NAME_OF_TEMP_ROOT_FOLDER    = "01_AssignmentTemplate"
PAR_PATH_OF_ASSIGNFOLDER        = "../../01_Assignments"
PAR_ROOT_DIR                    = os.getcwd()
PAR_TEX_TEMPLATE_FILE           = "../../../../00_Templates/00_TEX_TEMPLATES/01_Assignment/AssignmentTexTemplate.tex"
PAR_TEX_FOLDER_IN_TEMP          = "00_TexDocs"
PAR_COURSEINFO_FILE             = ".CourseInfo"

#################################################################################################################
#   CLASS DEFINITIONS                                                                                           #
#################################################################################################################

#################################################################################################################
#   GLOBAL VARIABLES                                                                                            #
#################################################################################################################

#################################################################################################################
#   FUNCTION DEFINITIONS                                                                                        #
#################################################################################################################
def create_main_folder(folder_name):
    os.chdir(PAR_PATH_OF_ASSIGNFOLDER)
    existing_directories = os.listdir(os.getcwd())
    max_dir_num = -1
    for dir in existing_directories:
        if dir.startswith("."):
            continue
        dir_num = int(dir[:2])
        if dir_num > max_dir_num:
            max_dir_num = dir_num
    new_dir_number = max_dir_num + 1
    if len(str(new_dir_number)) == 1:
        str_dir_number = "0" + str(new_dir_number)
    else:
        str_dir_number = str(new_dir_number)
    name_of_new_folder = str_dir_number+"_"+folder_name
    os.mkdir(name_of_new_folder)
    os.chdir(PAR_ROOT_DIR)

    return name_of_new_folder

def copy_folders_from_template(name_of_assignment_folder):
    os.chdir(os.path.join(PAR_PATH_OF_TEMPFOLDER,PAR_NAME_OF_TEMP_ROOT_FOLDER))
    temp_directories = [dir for dir in os.listdir(os.getcwd()) if not dir.startswith(".")]
    os.chdir(os.path.join(PAR_ROOT_DIR,PAR_PATH_OF_ASSIGNFOLDER,name_of_assignment_folder))
    for dir in temp_directories:
        os.mkdir(dir)


# parse course code and name from the .CourseInfo file
def parse_course_information(keys):
    ret_list = []
    file_content = open(os.path.join("../../",PAR_COURSEINFO_FILE),"r").read()
    for key in keys:
        re_key = key+'="([a-zA-Z0-9\s_-]+)"'
        found_value_for_key = re.search(re_key,file_content)
        if found_value_for_key:
            ret_list.append(found_value_for_key.group(1))
    return ret_list

# copy the template to the fresh new folders
def copy_tex_template(assign_name):
    # using id key will give back the identifier which should be used for the specific course, e.g. name or student id
    id = parse_course_information(['id'])
    filename = os.path.join(PAR_TEX_FOLDER_IN_TEMP,assign_name+"_"+id[0]+".tex")
    shutil.copyfile(PAR_TEX_TEMPLATE_FILE,filename)
    return filename

# generate information to the
def modify_tex_template(assign_name,file_name):
    course_details = parse_course_information(['code','name'])

    if len(course_details) < 2:
       return

    course_details[0] = course_details[0].replace('_','\\_') # avoid latex compile error

    default_title_text = 'title{}'
    basetext = '''title{assignname\\\\\n\\normalsize{coursecode - coursename}}\n'''

    mod_title_text = basetext.replace('assignname',assign_name)
    mod_title_text = mod_title_text.replace('coursecode',course_details[0])
    mod_title_text = mod_title_text.replace('coursename',course_details[1])
    file_content = open(file_name,'r').read()

    file_content = file_content.replace(default_title_text,mod_title_text)

    with open(file_name,'w') as fout:
        fout.write(file_content)

def compile_tex_file(file_name):
    os.chdir(PAR_TEX_FOLDER_IN_TEMP)
    file_name = file_name[file_name.find('/')+1:]
    command = 'xelatex ' + file_name
    os.system(command)


#################################################################################################################
#   MAIN                                                                                                        #
#################################################################################################################
if __name__=="__main__":
    TIME_START  = time.time()
    # beginning of body of main

    # parse name of the assignment to create folders
    assignment_name = raw_input("Please provide the name of the Assignment:")
    new_folder_name = create_main_folder(assignment_name)
    copy_folders_from_template(new_folder_name)
    tex_file = copy_tex_template(assignment_name)
    modify_tex_template(assignment_name,tex_file)
    compile_tex_file(tex_file)

    # end of body of main
    TIME_END    = time.time()
    # print execution time
    print("--- %s seconds ---" % (TIME_END - TIME_START))
    pass
#################################################################################################################
#   UNIT TESTS                                                                                                  #
#################################################################################################################
