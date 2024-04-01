def activity_selection(activities): 
    

    activities.sort(key=lambda activity: activity[1])

    included_activities = []
    included_activities.append(activities[0])

    for i in range(1, len(activities)):

        if activities[i][0] >= included_activities[-1][1]:
            included_activities.append(activities[i])

    return included_activities

def get_activities():
 
  activities = []
  while True:
    try:
      start_time, end_time = map(int, input("Enter start and end time (separated by space) or 'q' to quit: ").split())
      activities.append((start_time, end_time))
    except ValueError:
      if input("Invalid input. Enter 'q' to quit or press Enter to continue: ").lower() == 'q':
        break
  return activities

activities = get_activities()

print(activity_selection(activities))
