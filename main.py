from AccommodationByCommuteTime import AccommodationByCommuteTime

accom = AccommodationByCommuteTime()

accom.add_key_location("Snow Center (mins)", 51.745124957779815, -0.4587803032423951)
accom.add_key_location("Marlow (mins)", 51.573562647038216, -0.7757205625316245)
accom.add_key_location("Covent Garden (mins)", 51.51304766650138, -0.12393490716236541)
accom.add_key_location("Shoreditch", 51.52339103820956, -0.07542011521449478)
accom.add_key_location("Canary Wharf", 51.50613846247118, -0.018943522896932907)

accom.find_commute_time("Walthamstow", 51.59393631189506, -0.0203426720674187)
accom.find_commute_time("Wood Green", 51.597189070350005, -0.10975062490917802)
accom.find_commute_time("Enfield", 51.6486183871406, -0.052147521154598406)
accom.find_commute_time("Edgeware", 51.61602113013159, -0.26435318744848413)

print(accom.df)