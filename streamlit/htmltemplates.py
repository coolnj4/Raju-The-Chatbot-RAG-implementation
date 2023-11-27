css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}

.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''

    <b> ANSWER : </b>
    <div class="message">{{MSG}}</div>
    <br>

'''

user_template = '''

    <b> Question :  </b>    
    <div class="message">{{MSG}}</div>
    <br>

'''


foot = f"""
<div style="
    position: fixed;
    bottom: 0;
    left: 30%;
    right: 0;
    width: 50%;
    padding: 0px 0px;
    text-align: relative;
">
    <p>©The Thinkers</a></p>
</div>
"""

footer_fix =  """
        <style>
        
        #MainMenu {visibility: hidden;
        # }
            footer {visibility: hidden;
            }
            .css-card {
                border-radius: 0px;
                padding: 30px 10px 10px 10px;
                background-color: #f8f9fa;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                margin-bottom: 10px;
                font-family: "IBM Plex Sans", sans-serif;
            }
            
            .card-tag {
                border-radius: 0px;
                padding: 1px 5px 1px 5px;
                margin-bottom: 10px;
                position: absolute;
                left: 0px;
                top: 0px;
                font-size: 0.6rem;
                font-family: "IBM Plex Sans", sans-serif;
                color: white;
                background-color: green;
                }
                
            .css-zt5igj {left:0;
            }
            
            span.css-10trblm {margin-left:0;
            }
            
            div.css-1kyxreq {margin-top: -40px;
            }
            
        </style>
        """
        
inline_margine = f"""
    <div style="display: flex; align-items: center; margin-left: 0;">
        <h1 style="display: inline-block;">PDF Analyzer</h1>
        <sup style="margin-left:5px;font-size:small; color: green;">beta</sup>
    </div>
    """
    