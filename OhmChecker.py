import easygui as eg


#resistance = raw_input("What is the resistance of your coil?")
#voltage = raw_input("What is the voltage of your battery?")
#amperage = float(voltage) / float(resistance)
#wattage = float(voltage) * float(amperage)
#print "Your amperage is " + str(amperage)
#print "Your wattage is " + str(wattage)

msg         = "Fill out the required fields"
title       = "Ohm's Law Calculator"
fieldNames  = ["Voltage","Resistance"]
fieldValues = []  # we start with blanks for the values
fieldValues = eg.multenterbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:  # do forever, until we find acceptable values and break out
    if fieldValues == None:
        break
    errmsg = ""

    # look for errors in the returned values
    for i in range(len(fieldNames)):
        if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])

    if errmsg == "":
        break # no problems found
    else:
        # show the box again, with the errmsg as the message
        fieldValues = eg.multenterbox(errmsg, title, fieldNames, fieldValues)

print ("Reply was:", fieldValues)
voltage = fieldValues[0]
resistance = fieldValues[1]


amperage = float(voltage) / float(resistance)
wattage = float(voltage) * float(amperage)
amps = str(amperage)
watts = str(wattage)

print amperage
print wattage

eg.msgbox(msg="Your amperage is " + amps + " and your wattage is " + watts, title = "Ohm's Law Calculator" )