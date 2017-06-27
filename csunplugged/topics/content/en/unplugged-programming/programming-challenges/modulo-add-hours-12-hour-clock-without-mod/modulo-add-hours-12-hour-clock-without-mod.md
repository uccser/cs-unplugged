# Add hours on a clock without using “mod” (12-hour clock)

## Requirement:

Write a program that adds hours on a clock without using the “mod” operator. You need to keep subtracting 12 from the new time (original time + hours to add) until the the new time is less than or equal to 12.

## Testing examples:

Your program should display the outputs shown in this table for the given inputs provided;

<table>
  <tr>
    <th>Input</th>
    <th>Output</th>
  </tr>
  <tr>
    <td>11<br>1</td>
    <td>The new time is 12 o’clock.</td>
  </tr>
  <tr>
    <td>11<br>4</td>
    <td>The new time is 3 o’clock.</td>
  </tr>
  <tr>
    <td>11<br>12</td>
    <td>The new time is 11 o’clock.</td>
  </tr>
  <tr>
    <td>11<br>72</td>
    <td>The new time is 11 o’clock.</td>
  </tr>
</table>
