'''Text Utility Application: It enables you to perform various operations on the text you entered'''

from email.policy import default
from string import punctuation
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

 
@app.route('/analyze', methods=['POST'])
def capital():
    
    if request.method=='POST':
         
         text = request.form.get('text1')       # get text from the user
         # get the value of the checkbuttons
         capital = request.form.get('capital')  
         punctuation = request.form.get('punctuation')
         newline = request.form.get('newline')
         removespace = request.form.get('removespace')

         # check if any checkbox is checked  
         if punctuation != None:
             analyzed=''
             punc = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
             for char in text:
                 if char not in punc:
                     analyzed+=char
             text=analyzed
        
         if capital != None:
            analyzed=''
            analyzed = text.upper()
            text=analyzed

         if newline != None:
            analyzed=''
            
            for char in text:
              if char != "\n" and char!="\r":
                  analyzed+= char
            text= analyzed            
        
         if removespace != None:
             analyzed=''
             for index,char in enumerate(text):
                 if not ( text[index]==" " and text[index+1] ==' '):
                     analyzed+=char
             text= analyzed
            
    return render_template('analyze.html',text1=text)


if __name__ == '__main__':
    app.run(debug=True)