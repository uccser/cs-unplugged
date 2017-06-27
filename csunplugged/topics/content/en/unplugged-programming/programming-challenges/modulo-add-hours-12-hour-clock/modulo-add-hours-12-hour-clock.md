# Add hours on a clock (12-hour clock)

## Requirement:

Write a program that adds hours on a clock; for example, on a 12-hour clock, 11 o'clock plus 3 hours is 2 o'clock. This can be done using the modulo operator, except you need to adjust the output so that 0 in mod 12 is displayed as 12. See [challenge "Add hours on a clock (24-hour clock)"]('topics:programming_challenge' 'unplugged-programming' 'modulo-add-hours-24-hour-clock') if a 24-hour clock is usual in your country.

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
