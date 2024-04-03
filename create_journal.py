import os
import sys

def join_md_files(directory: str, output_file: str, mentee: str, mentor: str):
    """Join all .md files in a directory into a single .md file.
    
    Args:
        directory (str): The directory containing the .md files.
        output_file (str): The output file.
        mentor (str): The mentor's name and surname.
        mentee (str): The mentee's name and surname.
    """
    with open(output_file, 'w') as outfile:
        outfile.write("# SuperHero Valley Mentorship Program\n\n")
        outfile.write(f"Mentee: {mentee}\n")
        outfile.write(f"Mentor: {mentor}\n\n")

        for filename in os.listdir(directory):
            if filename.endswith(".md"):
                with open(os.path.join(directory, filename), 'r') as infile:
                    lines = infile.readlines()
                    outfile.writelines(lines[:])
                outfile.write("\n\n")


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print(sys.argv)
        print("Usage: python create_journal.py <mentee> <mentor>")
        sys.exit(1)

    mentee = sys.argv[1]
    mentor = sys.argv[2]

    join_md_files("./journal", "journal.md", mentee, mentor)