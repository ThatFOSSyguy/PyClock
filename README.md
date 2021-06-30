# PyClock
Simple, light-weight and FOSS clock build using Python

## Table of content
  1. <a href="https://github.com/ThatFOSSyguy/PyClock#supported-os">Supported OS</a>
  2. <a href="https://github.com/ThatFOSSyguy/PyClock#installation">Installation</a>
  3. <a href="https://github.com/ThatFOSSyguy/PyClock#getting-the-files-source-code">Getting the file's source-code and building from source</a>
  4. <a href="https://github.com/ThatFOSSyguy/PyClock#donation">Donations</a>


![image](https://user-images.githubusercontent.com/77693447/119951166-44429000-bfb9-11eb-85de-8a68657c528d.png)

# Supported OS
For now, PyClock only support's Windows 10. If you're using MacOS or Linux, please check the downloading the source-code and building from it.

# Installation
1. Click on "Releases" 

![image](https://user-images.githubusercontent.com/77693447/119951523-ab604480-bfb9-11eb-8d04-286e6db14bbb.png)

2. Click on the "PyClock-1.0.0.exe"

![image](https://user-images.githubusercontent.com/77693447/119952109-46f1b500-bfba-11eb-999f-3aca9e1a1fb9.png)

# Getting the file's source-code and building from source

You can use <a href="https://git-scm.com/">Git</a> to clone the repository if you have it. If incase you don't have Git you can follow the steps bellow to download the tarball

Step 1:
Download the tar ball file 

![image](https://user-images.githubusercontent.com/77693447/119855527-9ccd4b00-bf2f-11eb-85ad-aeedf8925585.png)

Step 2:
Opening the terminal in the file's directory and running this command:
```tar -xzvf PyClock-1.0.2.tar.gz```
```cd PyClock-1.0.2```

![image](https://user-images.githubusercontent.com/77693447/123828207-e63dfb00-d91e-11eb-89d5-0126f1ab44c9.png)

Step 3:
Now you should install Python as PyClock is build on Python.

_For windows users - If an error occures that ```python : The term 'python' is not recognized as the name of a cmdlet, function, script file, or operable program.```,
you might have not checked the option of adding Python to the path._

After installing Python, run ```pyinstaller -F -w -i clockIcon.ico clock.py```. Wait for few minutes for it to build, when it's finised building a message will pop up
that ```23069 INFO: Buliding EXE from EXE-00.toc completed sucessfully```. Now go to "dist" folder and double click on the "clock.exe" folder. If the build was
sucessful, the clock application will pop-up

_For windows users - Windows Defender will say it's a virus but it is just a false positive._

# Donation

Bitcoin:

```bc1qltshuqxpl0ewx49kx429vrtxd3gsw9ae3glqpp```

Monero:

```4A2GqdZW4edSMmPJ2nnXwMfdQqyk9xNVQN3S173kXHzjLd6g4cCczfsdFwq4miz5hfiDwjKnxC4MkQrzKMXgnfDzJQCsQRg```
