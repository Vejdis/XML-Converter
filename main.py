import xml.etree.ElementTree as ET

# initiera XML träd
root = ET.Element("people")


# Variabler som håller koll på nuvarande person och familjemdelem
current_person = None
current_family = None
current_address_parent = None  # Håll koll på om adressen till hör Person noden eller Familjemedlem noden
current_phone_parent = None  # Håll koll på om telefonen till hör Person noden eller Familjemedlem noden

# Öppna input filen
with open("input.txt", "r") as input_file:
    for line in input_file:
        parts = line.strip().split("|")
        category = parts[0] #Tar Kategorin av varje rad och väljer vad som ska göras

        if category == "P":
            # Skapa ny person P
            current_person = ET.SubElement(root, "person") # Skapa noden Person i root
            
            firstname = ET.SubElement(current_person, "firstname") # Skapa noden firstname i parent noden Person
            firstname.text = parts[1] #Lägg in texten från parts i den skapade noden
            
            lastname = ET.SubElement(current_person, "lastname") # Skapa noden lastname i parent noden Person
            lastname.text = parts[2] #Lägg in texten från parts i den skapade noden
            
            current_address_parent = current_person #Uppdatera vilken nod som adress ska in i ifall det kommer 
            current_phone_parent = current_person #Uppdatera vilken nod som telefon ska in i ifall det kommer

        elif category == "T":
            # Skapa ny telefon T
            phone = ET.SubElement(current_phone_parent, "phone") # Skapa noden phone i parent noden Person

            mobile = ET.SubElement(phone, "mobile") # Skapa noden mobile i parent noden phone
            if len(parts) > 1: #Verifiera att parts har indexet annars IndexError
                mobile.text = parts[1]

            landline = ET.SubElement(phone, "landline") # Skapa nodel landline i parent noden phone
            if len(parts) > 2: #Verifiera att parts har indexet annars IndexError
                landline.text = parts[2]

        elif category == "A":
            # Skapa ny adress A
            address = ET.SubElement(current_address_parent, "address") # Skapa noden address i parent noden Person
            
            street = ET.SubElement(address, "street") # skapa noden street i parent noden address i street
            if len(parts) > 1: #Verifiera att parts har indexet annars IndexError
                street.text = parts[1]
            
            city = ET.SubElement(address, "city") #Skapa noden city i parent noden address
            if len(parts) > 2: #Verifiera att parts har indexet annars IndexError
                city.text = parts[2]
            
            zip_code = ET.SubElement(address, "zip") # Skapa noden zip i parent noden address
            if len(parts) > 3: #Verifiera att parts har indexet annars IndexError
                zip_code.text = parts[3]
        elif category == "F":
            # Skapa ny familjemedlem F
                current_family = ET.SubElement(current_person, "family") # Skapa noden family i parent noden Person
                
                name = ET.SubElement(current_family, "name") # Skapa noden name i parent noden family
                if len(parts) > 1: #Verifiera att parts har indexet annars IndexError
                    name.text = parts[1] # Lägg in txten från parts i den skapade noden
                
                born = ET.SubElement(current_family, "born") # Skapa noden born i parent noden family
                if len(parts) > 2: #Verifiera att parts har indexet annars IndexError
                    born.text = parts[2]

                current_address_parent = current_family
                current_phone_parent = current_family
        else:
            # Hoppar andra katerogier loggar att det fanns en okänd kategori med
            print("Okänd kategori")
            pass

# Skapa ElementTree och spara det till en XML fil
tree = ET.ElementTree(root)
tree.write("output.xml", encoding="utf-8", xml_declaration=True)

print("XML fil har skapats")
