# PyClock
Simple, light-weight and FOSS clock build using Python

![image](https://user-images.githubusercontent.com/77693447/119951166-44429000-bfb9-11eb-85de-8a68657c528d.png)

# Supported OS
For now, PyClock only support's Windows 10. If you're using MacOS or Linux, please check the building instructions (https://github.com/ThatFOSSyguy/PyClock/blob/main/README.md#building-from-source)

# Installation 
1. Click on "Releases" 

![image](https://user-images.githubusercontent.com/77693447/119951523-ab604480-bfb9-11eb-8d04-286e6db14bbb.png)

2. Click on the "PyClock-1.0.0.exe"

![image](https://user-images.githubusercontent.com/77693447/119952109-46f1b500-bfba-11eb-999f-3aca9e1a1fb9.png)

# Building from source
Step 1:
Installing Python by going to www.python.org (For Windows users: Make sure that you have to add path in the installation). After the installation run ```python3```(For windows users ```python```) and ```pip3```(For windows users ```pip```)in the terminal/cmd. If an error occures then check YouTube for the installation steps for your operating system.

Step 2: 
Make sure that pyinstaller is there. To check run ```pyinstaller --version```. If an error occours, run ```pip install pyinstaller``` and the run ```pyinstaller --version``` again.

Step 3:
Download the tar.gz file 

![image](https://user-images.githubusercontent.com/77693447/119855527-9ccd4b00-bf2f-11eb-85ad-aeedf8925585.png)

Step 4:

Click on "Show in folder" 

![image](https://user-images.githubusercontent.com/77693447/119855756-d00fda00-bf2f-11eb-9cfa-b79713e8a37b.png)

Step 5:
Extract the file.

Step 6: 
Go to "PyClock-1.0.0.tar"

![image](https://user-images.githubusercontent.com/77693447/119858846-778e0c00-bf32-11eb-9d32-c6b4a4e64300.png)

And then to PyClock-1.0.0 folder

![image](https://user-images.githubusercontent.com/77693447/119859065-a86e4100-bf32-11eb-905a-e21910c4a047.png)

And for the last, copy the path

![image](https://user-images.githubusercontent.com/77693447/119859243-d6ec1c00-bf32-11eb-9064-1bc3b1e7a4e6.png)

Step 7: 
Open terminal/cmd and type ```cd``` + the copied path and hit enter.

![image](https://user-images.githubusercontent.com/77693447/119859614-2c282d80-bf33-11eb-8020-3fff93284f2c.png)

Step 8:
Type ```pyinstaller -F -w -i clockIcon.ico clock.py``` and hit enter. Wait for few minutes for it to build, when it's finised building a message will pop up that ```23069 INFO:
Buliding EXE from EXE-00.toc completed sucessfully```

Step 9: 
Go to "dist" folder and doubble click on the "clock.exe" folder. If a window pops up, you have sucessfully installed PyClock

# Donation

Bitcoin:

```bc1qltshuqxpl0ewx49kx429vrtxd3gsw9ae3glqpp```

Monero:

```4A2GqdZW4edSMmPJ2nnXwMfdQqyk9xNVQN3S173kXHzjLd6g4cCczfsdFwq4miz5hfiDwjKnxC4MkQrzKMXgnfDzJQCsQRg```
