# sequenze_grapher
Module to calculate and plot mathematical sequences in a given origin range.

## Usage:
1. Install the required modules: <br/>
`pip install -r requirements.txt` <br/><br/>
2. Execute `main.py` with your sequence as an argument: <br/>
`main.py -s <sequence> -r <origin range> -p <boolean: plot>`


## Example:
```main.py -s n*sin(n)-n**2 -r 200 -p True```

This will plot the sequence n * sin(n) - n ** 2 for an input range of `1 to 200`.
