# How to use a Python Script in Command Line
## Suzette Palmer
1. Create a Text File:
- Open your terminal (For Mac, go to "Launchpad" and type "terminal").
- Once open, navigate to where you would like to set up your script
	- For beginners, I would recommend moving to your Desktop. 
- To navigate to the Desktop, use the command:
```
cd Desktop

```
- Now to create a text file, use the following command:
```
touch relative_abundance.py

```
- Now type in the following URL to your browser 
```
https://github.com/suziepalmer10/MetagenomicsHelperScripts
```
- click on relative_abundance.py 
- In the right corner, click on the button that displays "copy raw contents" when you hover over it. 
- Paste this script into your relative_abundance.py file. 	

2. Update pip and install required libraries. Type these commands into your terminal. 

```
python -m pip install --upgrade pip
python -m pip install numpy pandas

```
3. Use the script with the following format, by typing in the modified command into the terminal:
python relative_abundance.py <path to level-5.csv> <output file path/name>
- To run a python script, you need to use the word "python" before
- Next, you type in the name of the script. Make sure that you are in the same directory as where the script is. For instance, if you have the script on your Desktop, you should also be navigate to your Desktop to run this command. 
- Insert the path where the input file is. To make this easier at first, keep your input file in the same directory as where your script is stored. 
- Insert the path where the output file should be, along with the name. To make this easier at first, keep your input file in the same directory as where your script is stored. 
An example command:
```
python relative_abundance.py /home2/s180020/Desktop/Gut_BSI_16S_Data/OutputFile_noclinda7/level-5.csv /home2/s180020/Desktop/outfile.csv

```
4. View your output file. 
5. Other helpful commands
- Navigate through directories (folders) --> move forward:
```
cd <foldername>

```
- Return to home directory 
```
cd

```
- Move one directory backward 
```
cd ..

```
- Get the path that your file is stored
```
pwd

```
- Make a folder
```
mkdir <foldername>

```

