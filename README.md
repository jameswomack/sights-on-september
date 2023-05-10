# Sights on September

A brief beautiful foray into computer vision

## Technologies involved

- ChatGPT (for research)
- VS Code intellisense (for research)
- AWS Rekognition
- python3 + pip3
- opencv
- click (for CLI interface)
- numpy

```sh
# EVERYTHING HERE EXCEPTING find_features_homography requires you to have 
# an active AWS setup. Most require an S3 bucket and 1 requires a Rekognition
# project to have been trained

python3 ./upload_file_to_s3.py sights-on-september ./data/input/visual/players/jordan-lawlar/2023-bowman-chrome_prospect.png 
# File uploaded successfully to s3://sights-on-september/2023-bowman-chrome.png


# ENSURE IMAGES ARE UPLOADED TO THE S3 BUCKET
python3 ./compare_faces_in_s3.py sights-on-september 2023-bowman-chrome.png 2023-bowman-chrome_prospect.png
# The faces match with a similarity score of 99.8832015991211%


# ENSURE IMAGES ARE UPLOADED TO THE S3 BUCKET
python3 ./compare_faces_in_s3.py sights-on-september 2023-bowman-chrome.png 66_rhys-hoskins_aligned_grey.png
# The faces do not match


# ENSURE IMAGES ARE UPLOADED TO THE S3 BUCKET
python3 ./detect_text_in_s3.py sights-on-september card_2023-bowman-chrome_prospect.png
# BOWMAN PRESENTS...
# MODERN
# PROSPECTS
# A
# LEAGUE
# OF HIS
# OWN
# ZONA
# JORDANSO
# LAWLAR


# ENSURE IMAGES ARE UPLOADED TO THE S3 BUCKET
python3 ./detect_text_in_s3.py sights-on-september corey_seager_2022_topps_back.png
#LA
#COREY SEAGER
#LOS ANGELES DODGERS® I SS
#301
#®
#HT: 6'4" WT: 215 BATS: LEFT THROWS: RIGHT DRAFTED: DODGERS #1-JUNE, 2012
#SERIES ONE
#ACQ: VIA DRAFT BORN: 4-27-94, CHARLOTTE, NC HOME: CONCORD, NC
#Staying healthy has been a challenge for Corey, but he reached the 2021 MLB All-Star Game
#break with the second-highest OPS (.857; 2,000+ PAs) of any shortstop since his debut six
#years earlier.


python3 ./find_features_homography.py ./data/input/visual/sets/2023_bowman_paper/10_trea-turner_grey.png ./data/input/visual/sets/2023_bowman_paper/66_rhys-hoskins_aligned_grey.png
# INFO:root:find_features_homography: [[ 1.16755909e+00  4.02645409e-02 -2.06306409e+02]
# [ 5.63499744e-02  1.30507901e+00 -4.91464005e+02]
# [ 5.70771056e-06  5.73040985e-05  1.00000000e+00]]
# 
# ... -> also writes an image demonstrating matching areas to the file system


# NEED TO START https://us-east-2.console.aws.amazon.com/rekognition/custom-labels?region=us-east-2#/projects/YourProjectName/models/YourModelName
AWS_REKOGNITION_ARN=arn:aws:rekognition:... python3 ./detect_logo_in_s3.py sights-on-september card_2023-bowman-chrome_sights.png
# bowman_chrome_logo 79.46399688720703
# Logo is not present in the image with confidence 100.00%
```
