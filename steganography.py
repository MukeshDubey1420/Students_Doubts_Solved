from steganography.steganography import Steganography

Steganography.encode('input.jpg','output.jpg','helllo')
text = Steganography.decode('output.jpg')
print text
print text