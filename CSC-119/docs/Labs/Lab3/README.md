# Lab 3
_Prepared for: CSC-119 Students_ /
_Prepared by: Marshall Gaucher_

**Due: 9/27/17 at 11:59 PM MT**

## Part 1: STQ From Textbook
STQ = Self-Test Questions

> :blue_book: Section 3.2.6: Questions 1, 2, 3, 6, 7

> :blue_book: Section 3.3.4: Questions 1, 4, 5

> :blue_book: Section 3.4.6: Questions 1, 2, 3, 4, 5, 6

## Part 2: Functions
### Introduction
Recall In Class Program 5, we calculated some temperature conversions. Now we want to expand on
that using our knowledge we obtained from Chapter 3. Below are some useful formulas and information
that will aid in you in this Lab:

| Conversion | Formula |
| **Fahrenheit** | --- |
| Fahrenheit to Celsius | Celsius = (Fahrenheit – 32) * 5/9 |
| Fahrenheit to Kelvin | Kelvin = (Fahrenheit + 459.67) * 5/9 |
| Fahrenheit to Rankine| Rankine = Fahrenheit + 459.67 |
| **Celsius** | --- |
| Celsius to Fahrenheit| Fahrenheit = Celsius * 9/5 + 32 |
| Celsius to Kelvin | Kelvin = Celsius + 273.15 |
| Celsius to Rankine| Rankine = (Celsius + 273.15) * 9/5 |
| **Kelvin** | --- |
| Kelvin to Fahrenheit| Fahrenheit = Kelvin * 9/5 – 459.67 |
| Kelvin to Celsius | Celsius = Kelvin – 273.15 |
| Kelvin to Rankine | Rankine = Kelvin * 9/5 |
| **Rankine** | --- |
| Rankine to Fahrenheit | Fahrenheit = Rankine – 459.67 |
| Rankine to Celsius | Celsius = (Rankine – 491.67) * 5/9 |
| Rankine to Kelvin | Kelvin = Rankine * 5/9 |


### Procedure

1. Print a program greeting (e.g. Generally describe what this program does)
2. Prompt the user to enter a temperature.
3. Prompt the user to enter a valid unit of temperature
   - (e.g. F = Fahrenheit, C= Celsius, K =Kelvin, R= Rankine)
4. If the user does not enter a valid unit of temperature
   - output “Invalid temperature unit”
5. If the user enters a value below the absolute zero for the given unit of temperature
   - output “Invalid temperature range for <temp unit> “
     (Example: user enters -3999 and K, print “Invalid temperature range for Kelvin”)
6. If the user enters F
   - Calculate Fahrenheit to Celsius
     - print(Fahrenheit, “F \xb0 equals “, format(Celsius, ‘.2f’), “C \xb0”)
   - Calculate Fahrenheit to Kelvin
     - print(Fahrenheit, “F \xb0 equals “, format(Kelvin, ‘.2f’), “K”)
   - Calculate Fahrenheit to Rankine
     - print(Fahrenheit, “F \xb0 equals “, format(Rankine, ‘.2f’), “R \xb0 ”)
7. If Fahrenheit >= Fahrenheit Boiling Point
   - print(Fahrenheit, “F \xb0 is Hot”)
8. If Fahrenheit <= Fahrenheit Freezing Point
   - print(Fahrenheit, “F \xb0 is Cold”)
9. If the user enters C
   - Calculate Celsius to Fahrenheit
     - print(Celsius, “C \xb0 equals “, format(Fahrenheit, ‘.2f’), “F \xb0”)
   - Calculate Celsius to Kelvin
     - print(Celsius, “C \xb0 equals “, format(Kelvin, ‘.2f’), “K”)
   - Calculate Celsius to Rankine
     - print(Celsius, “C \xb0 equals “, format(Rankine, ‘.2f’), “R \xb0”)
10. If Celsius >= Celsius Boiling Point
    - print(Celsius , “C \xb0 is Hot”)
11. If Celsius <= Celsius Freezing Point
    - print(Celsius , “C \xb0 is Cold”)
12. If the user enters K
    - Calculate Kelvin to Fahrenheit
      - print(Kelvin, “K equals “, format(Fahrenheit , ‘.2f’), “F \xb0”)
    - Calculate Kelvin to Celsius
      - print(Kelvin, “K equals “, format(Celsius , ‘.2f’), “C \xb0”)
    - Calculate Kelvin to Rankine
      - print(Kelvin, “K equals “, format(Rankine , ‘.2f’), “R \xb0”)
13. if Kelvin >= Kelvin Boiling Point
    - print(Kelvin , “K is Hot”)
14. if Kelvin <= Kelvin Freezing Point
    - print(Kelvin , “K is Cold”)
15. If the user enters R
    - Calculate Rankine to Fahrenheit
      - print(Rankine, “R \xb0 equals “, format(Fahrenheit , ‘.2f’), “F \xb0”)
    - Calculate Rankine to Celsius
      - print(Rankine, “R \xb0 equals “, format(Celsius , ‘.2f’), “C \xb0”)
    - Calculate Rankine to Kelvin
      - print(Rankine, “R \xb0 equals “, format(Kelvin , ‘.2f’), “K”)
16. if Rankine >= Rankine Boiling Point
    - print(Rankine , “R \xb0 is Hot”)
17. if Rankine <= Rankine Freezing Point
    - print(Rankine , “R \xb0 is Cold”)

