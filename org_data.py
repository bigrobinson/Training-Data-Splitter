#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:31:37 2019

@author: Brian Robinson
"""

import os
import random
import shutil

def split_data(root_dir, sub_dirs, test_ratio=0.1, val_ratio=0.1):

# Function to split data and labels into train, test, and validation sets
# INPUTS:
# root_dir = path to top level directory where data and labels are stored
# sub_dirs = directories under root where data and labels for different classes
#            are kept--label directory must be named like <data_directory>_labels
# test_ratio = proportion of data held out for testing
# val_ratio = proportion of data held out for validation
# OUTPUTS:
# Returns void but creates images and labels directories with desired splits

    try:
        (test_ratio>0 and
         test_ratio<=1 and
         val_ratio>0 and
         val_ratio<=1 and
         test_ratio+val_ratio>0 and
         test_ratio+val_ratio<=1)
    except ValueError:
        print('Test and validation ratios and their sum must lie between 0 and 1')

    # Creat directories for train, test, and validation if they don't exist
    for data_type in ['images', 'labels']:
        if os.path.isdir(os.path.join(root_dir, data_type)):
            shutil.rmtree(os.path.join(root_dir, data_type))
        os.mkdir(os.path.join(root_dir, data_type))
        for dir_type in ['train', 'test', 'val']:
            os.mkdir(os.path.join(root_dir, data_type, dir_type))

    # Split files for each class into train, test, and validation

    # Create (or overwrite existing) text files
    train_txt = open(os.path.join(root_dir, 'train.txt'), 'w+')
    test_txt = open(os.path.join(root_dir, 'test.txt'), 'w+')
    val_txt = open(os.path.join(root_dir, 'val.txt'), 'w+')

    for images_dir in sub_dirs:

        images_files = os.listdir(os.path.join(root_dir, images_dir))
        num_images = len(images_files)
        print('The number of ' + images_dir + ' images is: ' + str(num_images))
        num_test = int(test_ratio*num_images)
        num_val = int(val_ratio*num_images)
        num_train = num_images - num_test - num_val

        # Populate training text file and images and labels directories
        for file in images_files[0:num_train]:
            if os.path.isfile(os.path.join(root_dir, images_dir+'_labels', file[:-3]+'txt')):
                train_txt.write(os.path.join(root_dir, 'images', 'train', file)+'\n')
                shutil.copy(os.path.join(root_dir, images_dir, file),
                            os.path.join(root_dir, 'images', 'train'))
                shutil.copy(os.path.join(root_dir, images_dir+'_labels', file[:-3]+'txt'),
                            os.path.join(root_dir, 'labels', 'train'))
            else:
                print('WARNING: Label file \n' +
                      os.path.join(root_dir, images_dir+'_labels', file[:-3]+'txt') +
                      '\n' + 'does not exist, go to next file')

        # Populate test text file and images and labels directories
        for file in images_files[num_train:num_train+num_test]:
            if os.path.isfile(os.path.join(root_dir, images_dir+'_labels', file[:-3]+'txt')):
                test_txt.write(os.path.join(root_dir, 'images', 'test', file)+'\n')
                shutil.copy(os.path.join(root_dir, images_dir, file),
                            os.path.join(root_dir, 'images', 'test'))
                shutil.copy(os.path.join(root_dir, images_dir+'_labels', file[:-3]+'txt'),
                            os.path.join(root_dir, 'labels', 'test'))
            else:
                print('WARNING: Label file \n' +
                      os.path.join(root_dir, images_dir+'_labels', file[:-3]+'txt') +
                      '\n' + 'does not exist, go to next file')

        # Populate validation text file and images and labels directories
        for file in images_files[num_train+num_test:num_images]:
            if os.path.isfile(os.path.join(root_dir, images_dir+'_labels', file[:-3]+'txt')):
                val_txt.write(os.path.join(root_dir, 'images', 'val', file)+'\n')
                shutil.copy(os.path.join(root_dir, images_dir, file),
                            os.path.join(root_dir, 'images', 'val'))
                shutil.copy(os.path.join(root_dir, images_dir+'_labels', file[:-3]+'txt'),
                            os.path.join(root_dir, 'labels', 'val'))
            else:
                print('WARNING: Label file \n' +
                      os.path.join(root_dir, images_dir+'_labels', file[:-3]+'txt') +
                      '\n' + 'does not exist, go to next file')

    train_txt.close()
    test_txt.close()
    val_txt.close()

    return

if __name__ == '__main__':

    test_ratio = 0.1
    val_ratio = 0.1
    root_dir = '$HOME/data/'
    sub_dirs = ['Class1',
                'Class2',
                'Class3',
                'Class4',
                'Negatives']

    split_data(root_dir, sub_dirs, test_ratio, val_ratio)
