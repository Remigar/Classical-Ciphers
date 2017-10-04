Name: Eric Lara
Programming Language: Python
Program usage:
python main.py <CIPHER> <KEY> <ENC/DEC> <INPUT FILE> <OUTPUT FILE>


example input:
python main.py PLF security ENC input.txt output.text

where input.txt contains:
thequickbrownfoxjumpedoverthelazydog
output.txt will contain:
afsvsargkbnxmgxuasnlsfmxcsafsmbxignh

main main.py PLF security DEC input.txt output.text
where input.txt contains the above ciphertext
output.txt will contain:
thequickbrownfoxiumpedoverthelazydog (i has replaced j)
