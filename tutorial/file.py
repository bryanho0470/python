from datetime import date

extract_date = date.today()
def save_to_file(filename, total_jobs):  
  
  file = open(f"{filename}.csv", "w", encoding="utf-8-sig")

  file.write("Position,Compnay,Location,URL\n")
  for job in total_jobs:
      file.write(f"{job['title']},{job['company']},{job['location']},{job['link']}\n")

  file.write(f"{extract_date}\n")
  file.close()
