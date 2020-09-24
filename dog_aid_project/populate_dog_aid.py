import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','dog_aid_project.settings')
import django
django.setup()
from dog_aid.models import User, UserProfile, DogBreed, Dog, VetType, Vet, DogEvent, DogEventType, Symptom, Illness

def populate():
    person_1 = add_user('Rick', 'rick_user@gmail.com', 'rick_dogaid_password')
    person_2 = add_user('Fiona', 'fiona_user@hotmail.com', 'fiona_dogaid_password')
    person_3 = add_user('Anne', 'anne_user@hotmail.com', 'anne_dogaid_password')

    user_profile1 = add_user_profile(person_1, 'profile_images/Rick_hcRrkXp.jpg')
    user_profile2 = add_user_profile(person_2, 'profile_images/Fiona.jpg')
    user_profile3 = add_user_profile(person_3, 'profile_images/Anne.jpg')

    breed_1 = add_breed('Border Terrier', 'Terrier')
    breed_2 = add_breed('King Charles Spaniel', 'Spaniel')
    breed_3 = add_breed('Whippet', 'Hound')
    breed_4 = add_breed('Cocker Spaniel', 'Spaniel')
    breed_5 = add_breed('Jack Russell', 'Terrier')
    breed_6 = add_breed('Dachshund', 'Hound')
    breed_7 = add_breed('Labradoodle', 'Mixed breed')
    breed_8 = add_breed('Golden Retriever', 'Hunting dog')
    breed_10 = add_breed('German Shepherd', 'Working dog')
    breed_11 = add_breed('Border Collie', 'Working dog')
    breed_12 = add_breed('Boxer', 'Molussus')
    breed_13 = add_breed('Cockapoo', 'Mixed breed')
    breed_14 = add_breed('Labrador Retriever', 'Hunting dog')
    breed_15 = add_breed('Pug', '')

    dog_1 = add_dog('Buzz', person_1, '2014-06-14', breed_1, 'dog_images/Buzz_stKtCAl.jpg')
    dog_2 = add_dog('Ash', person_2, '2009-07-09', breed_2, 'dog_images/Ash_E8g9PcU.jpg')
    dog_3 = add_dog('Chewie', person_3, '2017-11-17', breed_1, 'dog_images/Chewie_cKkkKNo.jpg')
    dog_4 = add_dog('Sam', person_1, '2009-03-19', breed_3, 'dog_images/Sam_kF69x21.jpg')
    dog_5 = add_dog('Ziggy', person_3, '2011-06-14', breed_4, 'dog_images/Ziggy_J3fLNke_t1R1X0Q.jpg')

    vet_type1 = add_vet_type('1', 'Primary')
    vet_type2 = add_vet_type('2', 'Secondary')
    vet_type3 = add_vet_type('3', 'Emergency')
    vet_type4 = add_vet_type('4', 'Other')

    vet_1 = add_vet("Goddard Veterinary Group Ewell", '02083936049', '150 Kingston Road, Ewell, Surrey, KT17 2ET',
                    vet_type1, person_1)
    vet_2 = add_vet("Ewell Veterinary Centre", '02083936056', '4 Langton Ave, Ewell, Epsom, Surrey, KT17 1LD',
                    vet_type2, person_2)
    vet_3 = add_vet("Vets4Pets Epsom", '01372746510', 'Inside Pets at Home, 40 East Street, Epsom, KT17 1HQ',
                    vet_type3, person_3)

    event_type1 = add_dog_event_type(1, 'Vet appointment')
    event_type2 = add_dog_event_type(2, 'Grooming')
    event_type3 = add_dog_event_type(3, 'Training')
    event_type4 = add_dog_event_type(4, 'Medicine')
    event_type5 = add_dog_event_type(5, 'Milestone')
    event_type6 = add_dog_event_type(6, 'Other')

    dog_event1 = add_dog_event('Buzz check-up', dog_1, 1, '2020-04-09', 'Took Buzz to vet for check-up.')
    dog_event2 = add_dog_event('Stripping', dog_1, 2, '2020-04-22', 'Took Buzz to be stripped.')
    dog_event3 = add_dog_event('Dog training 1', dog_1, 3, '2020-09-12', "Buzz's first dog training class")
    dog_event3 = add_dog_event('Birthday', dog_1, 3, '2020-06-14', "Buzz's 5th birthday")
    dog_event4 = add_dog_event('Dog training 1', dog_2, 3, '2020-09-20', "Ash's first dog training class")
    dog_event5 = add_dog_event('Grooming appointment', dog_2, 2, '2020-04-09', "Ash grooming appointment")
    dog_event6 = add_dog_event('Advocate due', dog_3, 4, '2020-05-12', "Chewie needs advocate")
    dog_event7 = add_dog_event('Learnt "sit"', dog_3, 5, '2020-01-10', 'Chewie learnt the command "sit"')
    dog_event8 = add_dog_event('Stripping', dog_3, 2, '2020-04-28', "Stripping appointment")
    dog_event9 = add_dog_event('Check-up', dog_4, 1, '2020-04-09', "Vet check-up for Sam")
    dog_event10 = add_dog_event('Grooming', dog_4, 2, '2020-04-28', "Grooming appointment")
    dog_event11 = add_dog_event('Vet', dog_5, 1, '2020-01-07', "Vet appointment for hurt paw")
    dog_event812= add_dog_event('Learnt "roll over"', dog_5, 5, '2020-04-28', 'Ziggy learnt to "roll over"')

    symptom1 = add_symptom('1', 'Coughing', 'Dog is continuously coughing', '')
    symptom2 = add_symptom('2', 'Vomiting', 'Dog is vomiting excessively', '')
    symptom3 = add_symptom('3', 'Difficulty breathing', 'Dog is breathing rapidly/having trouble breathing', '')
    symptom4 = add_symptom('4', 'Listlessness', 'Languid/spiritless', '')
    symptom5 = add_symptom('5', 'Heavy panting', 'Heavy/excessive panting, salivation', '')
    symptom6 = add_symptom('6', 'Collapse', 'Dog becomes unconscious', '')
    symptom7 = add_symptom('7', 'Inflammation', 'A part of the body becomes swollen, red and hot.', '')
    symptom8 = add_symptom('8', 'Increased urinating', 'Urinating more often.', '')
    symptom9 = add_symptom('9', 'Bleeding', 'Your dog is excessively bleeding from a wound.', '')
    symptom10 = add_symptom('10', 'Tick', "There is a tick attached to your dog's skin.", 'illness_images/tickbite.jpg')
    symptom11 = add_symptom('11', 'Expressing pain',
                            "Your dog is clearly in pain, e.g. crying/whimpering, limping, licking itself.", '')
    symptom12 = add_symptom('12', 'Diarrhoea', "", '')
    symptom13 = add_symptom('13', 'Retching', "Your dog is heaving as if vomiting, without anything coming out.", '')
    symptom14 = add_symptom('14', 'Itching', "Dog is excessively scratching itself.", '')
    symptom15 = add_symptom('15', 'Weak pulse', "Heart beating slower.", '')
    symptom16 = add_symptom('16', 'Red, blue or pale skin', "", '')
    symptom17 = add_symptom('17', 'Shivering', "Your dog is shaking excessively.", '')
    symptom18 = add_symptom('18', 'Muscle stiffness', "Muscles become tight and is difficult to move.", '')
    symptom19 = add_symptom('19', 'Dilated pupils', "Pupils widened.", '')
    symptom20 = add_symptom('20', 'Salivating', "Drooling.", '')
    symptom21 = add_symptom('21', 'Blistered skin', "Skin becomes red, dry, peeling.", '')
    symptom22 = add_symptom('22', 'Blood in urine', "There is blood in your dog's urine.", '')
    symptom23 = add_symptom('23', 'Fever', "High temperature, vomiting, lethargic, shivering.", '')
    symptom24 = add_symptom('24', 'Not eating or drinking', "Refusing food or drink, or unable to keep it down.", '')
    symptom25 = add_symptom('25', 'Pawing at mouth', "Dog is continually pawing at their mouth, often in distress.", '')
    symptom26 = add_symptom('26', 'Expressing distress', "Pacing around, pawing at themselves.", '')

    illness1 = add_illness('1', 'Allergic reaction', "Allergic reaction is the body's way of reacting to an 'invader'. "
                                                     "\n\nWhen the body sense a foreign substance, called an antigen the immune system is triggered",
                           '', 'Cool the area with an ice pack or apply anti-histamine gel or cream.', 'No')
    illness2 = add_illness('2', 'Sunstroke or Heatstroke', 'Dogs cannot lose heat by sweating. '
                            'Heatstroke is one of the most common causes of avoidable canine death',
                           'illness_images/heatstroke_sunstroke.jpg',
                           'Immediately take your dog to a shady, cool area. '
                           '\n\nOffer the dog some water to drink. \n\nWrap the dog in a towel soaked in cold water.',
                           'No')
    illness3 = add_illness('3', 'Hypothermia', 'Most likely to occur if your dog has been in freezing water. '
                                               '\n\nCan also result from shock, after anaesthesia, and in newborn puppies',
                           'illness_images/hypothermia_exXweBt.jpg',
                           'Wrap your dog in warm blanket. Keep warm but avoid overheating',
                           "\n\nTake your dog's temperature, rectally if you can, and if it is below 37 degrees, "
                           "get immediate veterinary help.")
    illness4 = add_illness('4', 'Insect bite', 'Dog has been bitten by an insect.', '',
                           'If you can see the insect stinger, carefully remove it. '
                           '\n\nApply an icepack to the swelling, or a half vinegar half water solution. '
                           '\n\nPress a layer of onion to the affected area to reduce swelling.',
                           "If the sting is in the throat or mouth, or around the mouth, and is  causing difficulty breathing, "
                           "take your dog to the vet immediately. "
                           "Apply ice to the area on the way to keep it cool and reduce swelling.")
    illness5 = add_illness('5', 'Snake bite',
                           'Snake bites are rarely seen as they happen, but may have occurred if your dog is '
                           'trembling, excited, drooling, vomiting, has dilated pupils, or has collapsed.', '',
                           'Keep your dog calm. \n\nApply an icepack to wound to slow blood flow.',
                           "Yes. Carry your dog to the vet gently, as movement will increase blood flow.")
    illness6 = add_illness('6', 'Sunburn',
                           'Dogs with pale-coloured skin are at risk of sunburn, and related illnesses, e.g. skin cancer.',
                           '', 'Cool the area with an ice pack. Apply a gel containing anti-histamine.',
                           "If the sunburn is very serious, take your dog to the vet.")
    illness7 = add_illness('7', 'Frostbite',
                           'Extreme temperatures can lead to localised frostbite on extremities such as tips '
                           'of ears, tail, paws, testicles, nipples', '',
                           'Warm the area with tepid water around 32.3 degrees celsius.',
                           "Yes, immediately.")
    illness8 = add_illness('8', 'Cystitis',
                           'Inflammation of the bladder. Can be caused by a chill, e.g. after swimming, and '
                           'can be very painful.', '', 'Warm the area around the bladder with a hot water bottle. '
                                                       '\n\nGive your dog plenty of water to drink.',
                           "Yes, as they may need pain relief.")
    illness9 = add_illness('9', 'Burns',
                           'Can be caused by getting too close to hot steam or an open fire, or eating hot food or drink.',
                           '',
                           '1) First, treat any signs of shock. \n\n2) Cool the burn by holding under running cold water, followed by an ice pack. '
                           '\n\n3) Cover the area with a sterile bandage. \n\n4) Do not use ointments or powder.',
                           "Yes, immediately.")
    illness10 = add_illness('10', 'Bites or Cuts',
                            '4-6 hours after an injury, the wound will become contaminated, which can lead to infection.',
                            '', '', "")
    illness11 = add_illness('11', 'Tick bite',
                            'Ticks are parasitic arthropods that feed on the blood of their host. \n\nTicks tend to hide '
                            'out in tall grass or plants in wooded areas waiting for prospective hosts. \n\nThe tick climbs on to the host and attaches its'
                            'mouthparts into the skin to feed off the host. \n\nOn dogs they usually attach around the ears, in the area where the legs meet'
                            'the body, and between the toes.', 'illness_images/tickbite.jpg',
                            'The tick must be removed as soon as possible to avoid any possibility of'
                            'disease. The whole of the tick, including the mouthpiece must be fully removed. \n\nUse tweezers, or preferably a tick hook/tick'
                            'twister to clasp the tick tightly, and twist the tick until it detaches from your dog. \n\nDo not pull or squeeze the tick.',
                            "If you do not feel comfortable removing the tick yourself, take your dog to the vet and they will remove it. \n\nIf you attempt "
                            "to remove the tick yourself and the mouthpart remains, take your dog to the vet as soon as possible.")
    illness12 = add_illness('12', 'Vomiting',
                            "Vomiting is not always a sign of emergency. \n\nSometimes your dog simply eats too much, or eats something that"
                            "doesn't agree with them, or it may be caused by car sickness or nervousness.", '',
                            'Check temperature and the vomit and'
                            'faeces for blood, foreign bodies or parasites. \n\nFor isolated cases of vomiting, withdraw food for 24 hours but ensure fresh'
                            'water is always available. \n\nIf vomiting subsides over the following hours, the next day feed your dog 3-5 small meals which'
                            'consist of an easily digestible bland diet e.g. rice and chicken or scrambled egg.',
                            "If there is persistent vomiting and/or blood present in the vomit, take your dog to a vet immediately.")
    illness13 = add_illness('13', 'Diarrhoea',
                            'Most causes of vomiting can also give rise to diarrhoea, as the stomach and bowels are linked in both a'
                            'functional and anatomical sense.', '',
                            'Simple diarrhoea can usually be treated by fasting your dog for 24 hours, '
                            'followed by bland food e.g. chicken/scrambled egg and rice for a couple of days.',
                            "Diarrhoea must be treated by a vet if it is "
                            "explosive/painful, is black or contains blood, continues for longer than two days, is affecting the well-being of the dog, "
                            "is also accompanied by a high temperature, is very watery.")
    illness14 = add_illness('14', 'Swallowing foreign object',
                            'If your dog swallows a foreign object they may pass the object through '
                            'the stomach and intestines without difficulty, or the object can get stuck in the stomch or intestines '
                            'causing major problems. \n\nForeign objects can also become lodged in the throat, or pose a hazard to the soft '
                            'tissue in the stomach of throat.', '',
                            'If you see your dog swallow a foreign object, or suspect they '
                            'have, gently check their mouth and throat to see if the object has been lodged there and can be safely removed. '
                            '\n\nIf the object cannot be removed and your dog is breathing okay, immediately call your vet for further instruction.',
                            "Yes, if you cannot remove the object.")
    illness15 = add_illness('15', 'Choking',
                            'Dogs use their mouths to investigate, and can choke on just about anything, most commonly '
                            "small balls, bones, children's plastic toys", '',
                            'FOR A MEDIUM/LARGE DOG: \n\n1) Stand behind your dog, '
                            "place your arms around their body. \n\n2) Make a fist with one hand, and place against your dog's abdomen, where the "
                            "sternum ends. \n\n3) With the other hand, clasp your fist and push upward and froward (towads your dog's shoulders), "
                            "suddenly and forcefully. \n\nRepeat this 4 or 5 times, then check your dog's airways for debris from his mouth. "
                            "\n\nRepeat the chest thrusts if necessary. \n\nIf your dog stops breathing, clear the airway of any obstruction and perform "
                            "artificial respiration. \n\nFOR A SMALL DOG: \n\n1) Hold your dog against you with their head up, so that the spine is against "
                            "your chest. \n\n2) Make a fist with one hand, and place it against your dog's abdomen, just where the sternum ends. \n\n3) Grasp "
                            "the fist with your other hand, and give 4 or 5 rapids thrusts inward and upward. \n\n4) Check your dog's airways "
                            "and clear any debris form the mouth. \n\nRepeat the chest thrusts if necessary. \n\nIf your dog stops breathing, clear "
                            "the airway of any obstruction and perform artificial respiration. \n\nAFTER: Once the object has been removed, take your "
                            "dog to the vet immediately.", "Yes.")
    illness16 = add_illness('16', 'Fever', '', '', '', "")
    illness17 = add_illness('17', 'Poisoning', 'Certain substances and human foods can seriously affect the breathing, '
                                               'the skin, and the stomach and bowels, and can even be fatal. \n\nExamples include: \n- Anti-freeze '
                                               '\n- Insect poison \n- Weedkiller \n- Rat poison \n- Dyes \n- Paint \n- Tobacco \n- Human medicines '
                                               '\n- Chocolate \n- Some plants', '',
                            'Remove the potential source of poisoning. \n\nORAL POISONING: First '
                            "check they haven't swallowed any sharp objects, then give them a salt solution so they vomit up the "
                            "poison (3 tsps of salt in a glass of water).\n\nGASEOUS POISONING: If the poison is gaseous "
                            '(e.g. carbon monoxide) move the dog outside to the fresh air. \n\nON SKIN: If the poison is on the skin '
                            'bathe the area in clean, lukewarm water to wash it off. \n\nIf this is not possible, prevent the dog '
                            'from licking themselves with a medical collar, muzzle, blanket, or t-shirt. \n\nFAT, SOLUBLE SUBSTANCES: Such as'
                            ' tar can be removed with cooking oil. \n\nSTOPPED BREATHING: If the dog has stopped breathing carry '
                            'out resuscitation. \n\nVOMITED: If your dog has vomited, make sure to keep their airways clear, especially '
                            'if they are losing consciousness.',
                            "Yes, immediately. \n\nMost cases of poisoning require urgent treatment. "
                            "\n\nIf possible take a sample of the poisonous substance with you (even if in the form of vomit) so the "
                            "vet knows what they are dealing with.")

    python_symptom_to_illness = add_symptom_to_illness(illness1, symptom3)
    python_symptom_to_illness = add_symptom_to_illness(illness1, symptom14)
    python_symptom_to_illness = add_symptom_to_illness(illness1, symptom7)
    python_symptom_to_illness = add_symptom_to_illness(illness2, symptom5)
    python_symptom_to_illness = add_symptom_to_illness(illness2, symptom6)
    python_symptom_to_illness = add_symptom_to_illness(illness2, symptom16)
    python_symptom_to_illness = add_symptom_to_illness(illness2, symptom2)
    python_symptom_to_illness = add_symptom_to_illness(illness2, symptom12)
    python_symptom_to_illness = add_symptom_to_illness(illness2, symptom20)
    python_symptom_to_illness = add_symptom_to_illness(illness2, symptom17)
    python_symptom_to_illness = add_symptom_to_illness(illness3, symptom18)
    python_symptom_to_illness = add_symptom_to_illness(illness3, symptom17)
    python_symptom_to_illness = add_symptom_to_illness(illness3, symptom4)
    python_symptom_to_illness = add_symptom_to_illness(illness3, symptom3)
    python_symptom_to_illness = add_symptom_to_illness(illness3, symptom19)
    python_symptom_to_illness = add_symptom_to_illness(illness4, symptom11)
    python_symptom_to_illness = add_symptom_to_illness(illness4, symptom7)
    python_symptom_to_illness = add_symptom_to_illness(illness4, symptom14)
    python_symptom_to_illness = add_symptom_to_illness(illness5, symptom2)
    python_symptom_to_illness = add_symptom_to_illness(illness5, symptom17)
    python_symptom_to_illness = add_symptom_to_illness(illness5, symptom19)
    python_symptom_to_illness = add_symptom_to_illness(illness5, symptom6)
    python_symptom_to_illness = add_symptom_to_illness(illness5, symptom7)
    python_symptom_to_illness = add_symptom_to_illness(illness5, symptom20)
    python_symptom_to_illness = add_symptom_to_illness(illness6, symptom7)
    python_symptom_to_illness = add_symptom_to_illness(illness6, symptom21)
    python_symptom_to_illness = add_symptom_to_illness(illness7, symptom7)
    python_symptom_to_illness = add_symptom_to_illness(illness7, symptom21)
    python_symptom_to_illness = add_symptom_to_illness(illness7, symptom16)
    python_symptom_to_illness = add_symptom_to_illness(illness8, symptom8)
    python_symptom_to_illness = add_symptom_to_illness(illness8, symptom11)
    python_symptom_to_illness = add_symptom_to_illness(illness8, symptom26)
    python_symptom_to_illness = add_symptom_to_illness(illness8, symptom22)
    python_symptom_to_illness = add_symptom_to_illness(illness9, symptom7)
    python_symptom_to_illness = add_symptom_to_illness(illness9, symptom11)
    python_symptom_to_illness = add_symptom_to_illness(illness10, symptom9)
    python_symptom_to_illness = add_symptom_to_illness(illness10, symptom11)
    python_symptom_to_illness = add_symptom_to_illness(illness11, symptom10)
    python_symptom_to_illness = add_symptom_to_illness(illness12, symptom13)
    python_symptom_to_illness = add_symptom_to_illness(illness12, symptom2)
    python_symptom_to_illness = add_symptom_to_illness(illness12, symptom11)
    python_symptom_to_illness = add_symptom_to_illness(illness12, symptom7)
    python_symptom_to_illness = add_symptom_to_illness(illness14, symptom20)
    python_symptom_to_illness = add_symptom_to_illness(illness14, symptom2)
    python_symptom_to_illness = add_symptom_to_illness(illness14, symptom12)
    python_symptom_to_illness = add_symptom_to_illness(illness14, symptom23)
    python_symptom_to_illness = add_symptom_to_illness(illness14, symptom24)
    python_symptom_to_illness = add_symptom_to_illness(illness14, symptom25)
    python_symptom_to_illness = add_symptom_to_illness(illness15, symptom13)
    python_symptom_to_illness = add_symptom_to_illness(illness15, symptom25)
    python_symptom_to_illness = add_symptom_to_illness(illness15, symptom3)
    python_symptom_to_illness = add_symptom_to_illness(illness15, symptom26)
    python_symptom_to_illness = add_symptom_to_illness(illness16, symptom2)
    python_symptom_to_illness = add_symptom_to_illness(illness16, symptom4)
    python_symptom_to_illness = add_symptom_to_illness(illness16, symptom17)
    python_symptom_to_illness = add_symptom_to_illness(illness17, symptom2)
    python_symptom_to_illness = add_symptom_to_illness(illness17, symptom20)
    python_symptom_to_illness = add_symptom_to_illness(illness17, symptom1)
    python_symptom_to_illness = add_symptom_to_illness(illness17, symptom3)
    python_symptom_to_illness = add_symptom_to_illness(illness17, symptom4)
    python_symptom_to_illness = add_symptom_to_illness(illness17, symptom6)
    python_symptom_to_illness = add_symptom_to_illness(illness17, symptom26)
    python_symptom_to_illness = add_symptom_to_illness(illness17, symptom11)
    python_symptom_to_illness = add_symptom_to_illness(illness17, symptom17)

    for s in User.objects.all():
        print ("- {0}".format(str(s)))
    for s in UserProfile.objects.all():
        print("- {0}".format(str(s)))
    for s in DogBreed.objects.all():
        print("- {0}".format(str(s)))
    for s in Dog.objects.all():
        print("- {0}".format(str(s)))
    for s in VetType.objects.all():
        print("- {0}".format(str(s)))
    for s in Vet.objects.all():
        print("- {0}".format(str(s)))
    for s in DogEvent.objects.all():
        print("- {0}".format(str(s)))
    for s in DogEventType.objects.all():
        print("- {0}".format(str(s)))
    for s in Symptom.objects.all():
        print("- {0}".format(str(s)))
    for s in Illness.objects.all():
        print("- {0}".format(str(s)))

    s = User.objects.count()
    print("User - {0}".format(str(s)))
    s = UserProfile.objects.count()
    print("UserProfile - {0}".format(str(s)))
    s = DogBreed.objects.count()
    print("DogBreed - {0}".format(str(s)))
    s = Dog.objects.count()
    print("Dog - {0}".format(str(s)))
    s = VetType.objects.count()
    print("VetType - {0}".format(str(s)))
    s = Vet.objects.count()
    print("Vet - {0}".format(str(s)))
    s = DogEventType.objects.count()
    print("DogEventType - {0}".format(str(s)))
    s = DogEvent.objects.count()
    print("DogEvent - {0}".format(str(s)))
    s = Symptom.objects.count()
    print("Symptom - {0}".format(str(s)))
    s = Illness.objects.count()
    print("Illness - {0}".format(str(s)))

def add_user(username, email, password):
    p = User.objects.get_or_create(username=username, email=email, password=password)[0]
    return p

def add_user_profile(user, picture):
    p = UserProfile.objects.get_or_create(user=user, picture=picture)[0]
    return p

def add_breed(name, type):
    p = DogBreed.objects.get_or_create(name=name, type=type)[0]
    return p

def add_dog(name, owner, DOB, breed, picture):
    p = Dog.objects.get_or_create(name=name, owner=owner, DOB=DOB, breed=breed, picture=picture)[0]
    return p

def add_vet_type(vet_type_id, name):
    p = VetType.objects.get_or_create(vet_type_id=vet_type_id, name=name)[0]
    return p

def add_vet(name, phone_number, address, type, dog_owner):
    p = Vet.objects.get_or_create(name=name, phone_number=phone_number, address=address, type=type, dog_owner=dog_owner)[0]
    return p

def add_dog_event_type(dog_event_id, name):
    p = DogEventType.objects.get_or_create(dog_event_id=dog_event_id, name=name)
    return p

def add_dog_event(name, dog, event_type, date, notes):
    print (name, dog, event_type, date, notes)
    e_type = DogEventType.objects.get(dog_event_id=event_type)
    print ("e-type = ", e_type)
    p = DogEvent.objects.get_or_create(name=name, dog=dog, event_type=e_type, date=date, notes=notes)
    return p

def add_symptom(symptom_id, name, description, picture):
    p = Symptom.objects.get_or_create(symptom_id=symptom_id, name=name, description=description, picture=picture)[0]
    return p

def add_illness(illness_id, name, description, picture, treatment, call_vet):
    p = Illness.objects.get_or_create(illness_id=illness_id, name=name, description=description, picture=picture,
                                       treatment=treatment, call_vet=call_vet)[0]
    return p

def add_symptom_to_illness(illness, symptom):
    p = illness.related_symptom.add(symptom)
    return p

if __name__ == '__main__':
    print('Starting Dog Aid population script...')
    populate()
