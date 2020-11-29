# Clustering GMAIL email with extract category from TDIDF analysis

This notebook takes an archive of gmail messages and from them extracts the main information (body, header) in order to analyse them with textual or ml algorithm.

This first step is achieve by the function in the MailParser.py file

The second part is a TDIDF analysis tool that allows you to extract relevant words from the email and create clusters with them.

## Make it work

### requierement

To run the note book you need

Python 3.8.5

You also need those library :

* pandas

Install : `apt-get install python3-pandas`

* numpy, scipy, matplotlib

Install : `apt-get install python3-numpy python3-scipy python3-matplotlib`

* sklearn

Install : `apt-get install python3-sklearn`

### Getting your email

Download your email is really eazy, if you want some guidline below :

1. You’ll need to log into your Gmail account
2. Head to the ‘Download your data‘ page (https://takeout.google.com/settings/takeout). Here you’ll be able to select all the products to be included in your download.
3. All the products will be ‘Selected’ by default. If you want to start fresh, click ‘Select None‘.
4. Scroll down, find ‘Mail‘ and select it
5. All your email will be select, if you want only some email from a cetegory click on "All Mail data included" and select only those interesting category For our analyse we select email from personal and professional category. Those email will be download in separate file.

### Add your email file

To make the notebook work with your email add the personnal email in the data/input/personal_email folder and rename it Personal do the same for the professional one by adding them in data/input/professional_email folder and rename it Professional.

### Launch it

Your now ready to use the notebook. You have to open a terminal and go to the root folder of the notebook and type :

`python3 Main.py`
