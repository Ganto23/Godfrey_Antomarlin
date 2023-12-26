import shutil
import os
from os import scandir, rename
from os.path import splitext, exists, join
import sys
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from time import sleep

file_extension_image = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.tiff', '.psd', '.raw', '.bmp', '.heif', '.indd']

file_extension_music = ['.3gp', '.aa', '.aac', '.aax', '.act', '.aiff', '.alac', '.amr', '.ape', '.au', '.awb', '.dss',
                        '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.m4p', '.mmf', '.movpkg', '.mp3', '.mpc',
                        '.msv', '.nmf', '.ogg', '.oga', '.mogg', '.opus', '.ra', '.rm', '.raw', '.rf64', '.sln', '.tta', 
                        '.voc', '.vox', '.wav', '.wma', '.wv', '.webm', '.8svx', '.cda']

file_extension_video = ['.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.drc', '.gif', '.gifv', '.mng', '.avi', '.mov'
                        '.qt', '.wmv', '.mp4', '.m4p', '.m4v', '.mpg', '.mpeg', '.mp2', '.mpv', '.flv']




source_dir = '?'
dest_dir_image = '??'
dest_dir_music = '???'
dest_dir_video = '????'
dest_dir_other = '?????'

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1

    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name

def move(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)



class MoverHandler(LoggingEventHandler):
    def on_modified(self,event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                ending = os.path.splitext(name)[1]
                if ending in file_extension_image:
                    dest = dest_dir_image
                    
                elif ending in file_extension_music:
                    dest = dest_dir_music
                    
                elif ending in file_extension_video:
                    dest = dest_dir_video
                    
                else:
                    dest = dest_dir_other
                move(dest, entry, name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
