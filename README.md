# facebook-login-page

This code creates a graphical user interface (GUI) for a mock Facebook login page using Tkinter, a Python library for building desktop applications. Here's a detailed description of the code:

**Importing Tkinter Library:**

The tkinter library is imported to create the GUI elements.
**Defining the Login Function:**

A function login() is defined to handle the login process.
It retrieves the username and password entered by the user.
If the credentials are 'admin' for both username and password, a new window titled 'feed' is opened.
If the credentials are incorrect, an error message is displayed within the login frame.
**Setting Up the Main Window:**

The main window (root) is created with the title 'Facebook log in'.
The window size is set to 1000x600 pixels.
**Creating the Login Frame:**

A frame (frame1) is created to hold the login form elements, positioned at specific coordinates.
A Text widget (uname_t) is created for the username input, with specific styling and placement.
A label for the username is added above the username input field.
A Text widget (pword_t) is created for the password input, with specific styling and placement.
A label for the password is added above the password input field.
A 'Login' button (log_btn) is created, which triggers the login function when clicked.
A label (fg_btn) is created for 'Forgot Password?' below the login button.
**Creating the Sign-Up Frame:**

Another frame (frame2) is created to hold the sign-up prompt, positioned at specific coordinates.
A button (creat_btn) is added to the sign-up frame, allowing users to create a new account.
**Adding Facebook Branding and Slogan:**

A label (fb) is created with the text 'facebook' styled to resemble the Facebook brand, positioned on the main window.
A label (stmt) is created with a slogan text, positioned below the Facebook label.
**Running the Main Loop:**

The root.mainloop() method is called to start the Tkinter event loop, making the window and its contents interactive.
