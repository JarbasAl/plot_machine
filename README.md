# The Plotto Plot Machine

A program to automate the algorithm described in <a href="https://openlibrary.org/works/OL16087095W/Plotto" target="_blank">William Wallace Cook's Plotto, The Masterbook of All Plots</a>.

## Install

    pip install plot_machine

## Usage

```python
from plot_machine import Plotto

p = Plotto().wild_combination()
p.print()

```

outputs

        The plot: 

        A Resentful Person, Being delivered from misfortune by one who, in confidence, confesses a secret of transgression, Rescues integrity from a serious entanglement.
        
        The Conflict:
        
        Married Life; Divorce
        
        Cast of characters: 
        
        Craig Tyson : male protagonist
        
        Patricia Neely : female protagonist
        
        Harriet Brown : female stranger
        
        Jill Waguespack : sister of Patricia Neely 
 
 

```python   
p = Plotto().wild_combination()
print(p.masterplot)
print(p.conflicts)
for character in p.cast:
    print(character.name, character.gender, character.role)
```
  
## Credits

The text of Plotto is obtained from: https://openlibrary.org/works/OL16087095W/Plotto.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

forked from [stuarthoye/The-Plotto-Plot-Machine](https://github.com/stuarthoye/The-Plotto-Plot-Machine)