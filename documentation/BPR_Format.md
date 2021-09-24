# BPR Format
## SGP Baltie Code file

### Header

The header is 6 bytes long.

`0x00-0x02 - BPR magic`  
`0x03 - version(?)`  
`0x04-0x05 - how many blocks`  

##### eg. Header:
`42 50 52 01 08 00`  
BPR File, Version 1, 8 Blocks of code

### The Code

#### -= Instruction Blocks =-
Each block is 4 bytes long. It represents instruction and it's corresponding bank.

##### eg. The "Walk Forwad" block looks like this:
`AD 8A 01 00`  
These bytes (in little endian) equals 101037 in decimal.  
The last 3 digits represent the tile number (in this case it's 037).
The rest represent the bank number (in this case it's 101).  
All instruction tiles are in bank 101 (from the .C** file).
(The tile number cannot be greater than 150!)

#### -= Scene Blocks =-
A scene block will appear infront of the character.  
Just like instruction blocks, it's stored in 4 bytes. It represents tile and it's corresponding bank.

##### eg. To place a tile with a letter "B", the block will look like this:
`55 04 00 00`  
These bytes (in little endian) equals 1109 in decimal.  
The last 3 digits represent the tile number (in this case it's 109).
The rest represent the bank number (in this case it's 1).  
If the decimal value is lower than 1000, it uses tiles from bank 0.
(The tile number cannot be greater than 150!)

##### Example code:
`A4 8A 01 00` `CC 8A 01 00` `AD 8A 01 00` `D1 8A 01 00` `9F 8A 01 00` `9D 8A 01 00` `CC 8A 01 00` `B2 8A 01 00`  
Which translates to:  
` Number 7,   Times [x],     Walk,    Face down,  Number 2,   Number 0,   Times [x], Wait 0.1 sec`

### Instruction Blocks

- `DA 8A 01 00 (101082)` - Empty space
- `AD 8A 01 00 (101037)` - Walk
- `AE 8A 01 00 (101038)` - Turn left
- `AF 8A 01 00 (101039)` - Turn right
- `B0 8A 01 00 (101040)` - Make Baltie invisible
- `B1 8A 01 00 (101041)` - Make Baltie visible
- `B2 8A 01 00 (101042)` - Wait 0.1 sec
- `B3 8A 01 00 (101043)` - Wait for any input
- `E0 8A 01 00 (101088)` - Disable cloud
- `E1 8A 01 00 (101089)` - Enable cloud
- `B4 8A 01 00 (101044)` - Clear/Load scene
- `B5 8A 01 00 (101045)` - Play a sound
- `D0 8A 01 00 (101072)` - Face right
- `D1 8A 01 00 (101073)` - Face down
- `D2 8A 01 00 (101074)` - Face left
- `D3 8A 01 00 (101075)` - Face up
- `CF 8A 01 00 (101071)` - Comment
- `97 8A 01 00 (101015)` - Set speed
- `9D 8A 01 00 (101021)` - Number 0
- `9E 8A 01 00 (101022)` - Number 1
- `9F 8A 01 00 (101023)` - Number 2
- `A0 8A 01 00 (101024)` - Number 3
- `A1 8A 01 00 (101025)` - Number 4
- `A2 8A 01 00 (101026)` - Number 5
- `A3 8A 01 00 (101027)` - Number 6
- `A4 8A 01 00 (101028)` - Number 7
- `A5 8A 01 00 (101029)` - Number 8
- `A6 8A 01 00 (101030)` - Number 9
- `CC 8A 01 00 (101068)` - Times [x]
- `CD 8A 01 00 (101069)` - Open bracket [(]
- `CE 8A 01 00 (101070)` - Close bracket [)]
- `DB 8A 01 00 (101083)` - Next line