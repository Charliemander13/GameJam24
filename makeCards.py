#to make this work, run "pip3 install Pillow"
#to make this work, run "pip3 install pandas"

from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import textwrap

# Fonts on the card
Title = ImageFont.truetype("fonts/BarlowCondensed-Medium.ttf", 64)

# Size of the card
width, height = 1050, 750

# Load the CSV file into a DataFrame
csvFile = 'cardData.csv' 
df = pd.read_csv(csvFile)

df = df.fillna('')

# Repeat this process on each card in the CSV
for index, row in df.iterrows():

	# Create the white base card
	card = Image.new('RGB', (width, height), 'white')
	draw = ImageDraw.Draw(card)
	
	# Access data using row names
	Theme1 = str(row['Theme 1'])
	Theme2 = str(row['Theme 2'])
	CardName = str(row['Name'])

	# Find the theme 1 color
	if str(row['Theme 1']) == 'Silly':
		Theme1Color = '#fae36a'

	elif str(row['Theme 1']) == 'Romantic':
		Theme1Color = '#f3bebb'

	elif str(row['Theme 1']) == 'Nostalgic':
		Theme1Color = '#ee7a4a'

	elif str(row['Theme 1']) == 'Political':
		Theme1Color = '#4e73b9'	
	
	elif str(row['Theme 1']) == 'Scary':
		Theme1Color = '#353439'

	elif str(row['Theme 1']) == 'Family':
		Theme1Color = '#668e43'

	elif str(row['Theme 1']) == 'Pop culture':
		Theme1Color = '#705d94'	

	elif str(row['Theme 1']) == 'Workplace':
		Theme1Color = '#955a3a'	

	elif str(row['Theme 1']) == 'Dramatic':
		Theme1Color = '#da473a'		
	
	else: 
		Theme1Color = 'white'

	# Find the theme 2 color
	if str(row['Theme 2']) == 'Silly':
		Theme2Color = '#fae36a'

	elif str(row['Theme 2']) == 'Romantic':
		Theme2Color = '#f3bebb'

	elif str(row['Theme 2']) == 'Nostalgic':
		Theme2Color = '#ee7a4a'

	elif str(row['Theme 2']) == 'Political':
		Theme2Color = '#4e73b9'	
	
	elif str(row['Theme 2']) == 'Scary':
		Theme2Color = '#353439'

	elif str(row['Theme 2']) == 'Family':
		Theme2Color = '#668e43'

	elif str(row['Theme 2']) == 'Pop culture':
		Theme2Color = '#705d94'	

	elif str(row['Theme 2']) == 'Workplace':
		Theme2Color = '#955a3a'	

	elif str(row['Theme 2']) == 'Dramatic':
		Theme2Color = '#da473a'		
	
	else: 
		Theme2Color = 'white'

	#Draw the left side color 
	draw.rectangle(xy = (0, 0, 175, 750), fill = (Theme1Color), outline = (0, 0, 0), width = 0) 

	#Draw the right side color 
	draw.rectangle(xy = (875, 0, 1050, 750), fill = (Theme2Color), outline = (0, 0, 0), width = 0) 
	
	iconSize = 200, 200

	#Import the theme icons
	SillyImage = Image.open(r"/Users/charliemackin/Documents/GitHub/GameJam24/IconsColor/Silly_Color.png").convert("RGBA").resize(iconSize)
	RomanticImage = Image.open(r"/Users/charliemackin/Documents/GitHub/GameJam24/IconsColor/Romantic_Color.png").convert("RGBA").resize(iconSize)
	NostalgicImage = Image.open(r"/Users/charliemackin/Documents/GitHub/GameJam24/IconsColor/Nostalgic_Color.png").convert("RGBA").resize(iconSize)
	PoliticalImage = Image.open(r"/Users/charliemackin/Documents/GitHub/GameJam24/IconsColor/Political_Color.png").convert("RGBA").resize(iconSize)
	ScaryImage = Image.open(r"/Users/charliemackin/Documents/GitHub/GameJam24/IconsColor/Scary_Color.png").convert("RGBA").resize(iconSize)
	FamilyImage = Image.open(r"/Users/charliemackin/Documents/GitHub/GameJam24/IconsColor/Family_Color.png").convert("RGBA").resize(iconSize)
	PopCultureImage = Image.open(r"/Users/charliemackin/Documents/GitHub/GameJam24/IconsColor/PopCulture_Color.png").convert("RGBA").resize(iconSize)
	WorkplaceImage = Image.open(r"/Users/charliemackin/Documents/GitHub/GameJam24/IconsColor/Workplace_Color.png").convert("RGBA").resize(iconSize)
	DramaticImage = Image.open(r"/Users/charliemackin/Documents/GitHub/GameJam24/IconsColor/Dramatic_Color.png").convert("RGBA").resize(iconSize)

	# Find Theme 1 and paste the theme icons
	if str(row['Theme 1']) == 'Silly':
		Image.Image.paste(card, SillyImage, (425, 0), SillyImage)

	elif str(row['Theme 1']) == 'Romantic':
		Image.Image.paste(card, RomanticImage, (425, 0), RomanticImage)

	elif str(row['Theme 1']) == 'Nostalgic':
		Image.Image.paste(card, NostalgicImage, (425, 0), NostalgicImage)

	elif str(row['Theme 1']) == 'Political':
		Image.Image.paste(card, PoliticalImage, (425, 0), PoliticalImage)
	
	elif str(row['Theme 1']) == 'Scary':
		Image.Image.paste(card, ScaryImage, (425, 0), ScaryImage)

	elif str(row['Theme 1']) == 'Family':
		Image.Image.paste(card, FamilyImage, (425, 0), FamilyImage)

	elif str(row['Theme 1']) == 'Pop culture':
		Image.Image.paste(card, PopCultureImage, (425, 0), PopCultureImage)

	elif str(row['Theme 1']) == 'Workplace':
		Image.Image.paste(card, WorkplaceImage, (425, 0), WorkplaceImage)
		
	else:
		Image.Image.paste(card, DramaticImage, (425, 0), DramaticImage)


	# Find Theme 2 and paste the theme icons
	if str(row['Theme 2']) == 'Silly':
		Image.Image.paste(card, SillyImage, (425, 550), SillyImage)

	elif str(row['Theme 2']) == 'Romantic':
		Image.Image.paste(card, RomanticImage, (425, 550), RomanticImage)

	elif str(row['Theme 2']) == 'Nostalgic':
		Image.Image.paste(card, NostalgicImage, (425, 550), NostalgicImage)

	elif str(row['Theme 2']) == 'Political':
		Image.Image.paste(card, PoliticalImage, (425, 550), PoliticalImage)
	
	elif str(row['Theme 2']) == 'Scary':
		Image.Image.paste(card, ScaryImage, (425, 550), ScaryImage)

	elif str(row['Theme 2']) == 'Family':
		Image.Image.paste(card, FamilyImage, (425, 550), FamilyImage)

	elif str(row['Theme 2']) == 'Pop culture':
		Image.Image.paste(card, PopCultureImage, (425, 550), PopCultureImage)

	elif str(row['Theme 2']) == 'Workplace':
		Image.Image.paste(card, WorkplaceImage, (425, 550), WorkplaceImage)
		
	else:
		Image.Image.paste(card, DramaticImage, (425, 550), DramaticImage)


	draw.text((525, 375), CardName, fill='black', anchor="mm",font= Title, align='center')

	# Save the card as a PNG file
	fileName = 'cards/'+str(row['Name'])
	card.save(fileName.title().replace(" ",'')+'.png')