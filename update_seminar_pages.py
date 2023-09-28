import numpy as np
import matplotlib.pyplot as plt

import os
import sys

import yaml



if __name__ == "__main__":
    
    # Load all seminar data 
    seminar_data = yaml.safe_load(open("seminar_talks.yml"))

    # Change to folder
    os.chdir("seminar_pages")

    # Remove all existing files
    for file in os.listdir():
        os.remove(file)

    # Make new files for all talks
    for key, data in seminar_data.items():

        fname = f"{key}.qmd"
        with open(fname, 'w') as file:
            file.write("---\n")
            file.write(f"title: \"{data['title']}\"\n")
            file.write("---\n")

            if data['speaker_url'] is None:
                speaker_str = f"{data['speaker']} ({data['affiliation']})"
            else:
                speaker_str = f"[{data['speaker']}]({data['speaker_url']}) ({data['affiliation']})"
            file.write(f"**Speaker:** {speaker_str}\n\n")
            file.write(f"**Date:** {data['date']}\n\n")
            file.write(f"**Abstract:** {data['abstract']}")
            



