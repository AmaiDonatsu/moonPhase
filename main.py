from lunapack.calendar import generate_calendar
from lunapack.computes import computePhases

if __name__ == '__main__':
    calendar_phases = computePhases(2024)
    generate_calendar(calendar_phases, month = 0)
    print(calendar_phases)


