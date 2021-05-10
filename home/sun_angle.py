def sun_angle(time):

    hour, minute = (time.split(':'))
    degree = 180*((int(hour)-6)*60+int(minute))/(12*60)

    return degree if (degree>=0)&(degree<=180) else "I don't see the sun!"
    # if (degree>=0)&(degree<=180):
    #     return degree

    # else:
    #     print("I don't see the sun!")
    #     return("I don't see the sun!")
        
print(1,sun_angle("05:59"))
print(2,sun_angle("06:00"))
print(3,sun_angle("09:30"))
print(4,sun_angle("12:00"))
print(5,sun_angle("18:00"))
print(6,sun_angle("18:01"))
print(7,sun_angle("66:00"))