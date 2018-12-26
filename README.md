# yahoo-finance
A crawler that fetches the stock history data from yahoo finance.

Run the code with
```
python3 main.py 
```
Don't forget to create a folder to store the data and change the path in main.py

If a stock failed , the Index will be saved in fail.txt, change line 8 in main.py from
```
firstcolumn = [line.rstrip() for line in f]  # line.split(',')[0]

to

firstcolumn = [line.split(',')[0] for line in f]
```

and re-run the test with the input file changed to fail.txt, this helps avoid dupicate download which is time consumming.
