import juliandate as jd

def calendarFormat (julian, phase):
    gregorian_date = jd.to_gregorian(julian)

    calendar_vignette = {
        "phase": phase,
        "year": gregorian_date[0],
        "month": gregorian_date[1],
        "day": gregorian_date[2],
        "hour": gregorian_date[3],
        "min": gregorian_date[4],
        "sec": gregorian_date[5],
        "mil": gregorian_date[6],
    }

    return calendar_vignette

