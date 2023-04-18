import hashlib, os, re, datetime, platform

#version 2.2
def gmd5hof(path):
  sha256_hash = hashlib.sha256()
  file_count = 0

  for file in os.listdir(path):
    if file_count >= 15:
      break
    file_path = os.path.join(path, file)
    if os.path.isdir(file_path):
      continue
    with open(file_path, 'rb') as f:
      file_contents = f.read()
      sha256_hash.update(file_contents)
    file_count += 1

  if file_count == 0:
    sha256_hash.update(
      'Empty folder but i dont want a empty hash'.encode('utf-8'))
    print('Empty folder:' + path)

  return sha256_hash.hexdigest()


def sum_decimal_digits(decimal_list):
  return sum(
    int(digit) for number in decimal_list for digit in str(number)
    if digit.isdigit())


def getquote(howmanytimes, key, key2):
  key = str(key)
  key2 = str(key2)
  p_quote = [
    "I'm different...", 'The cake is a lie!', "Oh, it's you",
    "It's been a long time", "How have you been?",
    "I've been really busy being dead", "You know, after you MURDERED Me!",
    "This was a triumph I'm making a note here; 'Huge success' It's hard to overstate My satisfaction Aperture Science: We do what we must Because we can For the good of all of us Except the ones who are dead But there's no sense crying Over every mistake You just keep on trying Till you run out of cake And the science gets done And you make a neat gun For the people who are Still alive I'm not even angry I'm being so sincere right now Even though you broke my heart, And killed me And tore me to pieces And threw every piece into a fire As they burned it hurt because I was so happy for you Now, these points of data Make a beautiful line And we're out of beta We're releasing on time So I'm GLaD I got burned Think of all the things we learned- For the people who are Still alive Go ahead and leave me I think I'd prefer to stay inside Maybe you'll find someone else To help you? Maybe Black Mesa? That was a joke Haha - Fat Chance Anyway this cake is great It's so delicious and moist Look at me: still talking When there's science to do When I look out there, It makes me GLaD I'm not you I've experiments to run There is research to be done On the people who are Still alive And believe me I am Still alive I'm doing science and I'm Still alive I feel fantastic and I'm Still alive While you're dying I'll be Still alive And when you're dead I will be Still alive Still alive",
    "Those of you who volunteered to be injected with praying mantis DNA, I've got some good news and some bad news. Bad news is we're postponing those tests indefinitely. Good news is we've got a much better test for you: fighting an army of mantis men. Pick up a rifle and follow the yellow line. You'll know when the test starts.",
    "Hello space gods!"
  ]
  if howmanytimes >= len(key):
    if howmanytimes >= len(key2):
      toolittlehashes = [7341925680572847327448]
      howmanytimes += 1
      return hashlib.shake_128(
        p_quote[toolittlehashes[howmanytimes]].encode()).hexdigest()
    else:
      backupnumbers = key2
      howmanytimes += 1
      return hashlib.sha512(p_quote[int(
        backupnumbers[howmanytimes])].encode()).hexdigest()
  else:
    howmanytimes += 1
    return hashlib.sha256(p_quote[int(key[howmanytimes])].encode()).hexdigest()


def cramp(min, max):
  # Get username of the user who's signed in and the name of the computer
  try:
    username = os.getlogin()
  except:
    username = 'Default'
  hostname = 'Default'
  # Hash the user and computer name
  husername = hashlib.sha256(username.encode()).hexdigest()
  hhostname = hashlib.sha256(hostname.encode()).hexdigest()
  # Get common folder's hashes
  try:
    hdownload = gmd5hof(f'C:\\Users\\{os.getlogin()}\\Downloads')
  except:
    hdownload = 'a69e07b1c51d972f4a97820c4cce4a6d'
  try:
    hdesktop = gmd5hof(f'C:\\Users\\{os.getlogin()}\\Desktop')
  except:
    hdesktop = '616d3fa65055ea0b114bd96cf816c973'
  # Hash together all common folder's hashes, then hash the user and hostname, then combine the two
  folders = hdownload + hdesktop
  hfolders = hashlib.sha256(folders.encode()).hexdigest()
  user = husername + hhostname
  hhuser = hashlib.sha512(user.encode()).hexdigest()
  together = hhuser + hfolders
  htogether = hashlib.sha224(together.encode()).hexdigest()
  key2 = ''.join(re.findall(r'\d+', hfolders))
  # Get all numbers from htogether and keep it as a key to use in the future
  key = ''.join(re.findall(r'\d+', htogether))
  key = str(key)
  # What is today's date, what hour is it, and how many 10 minute intervals has it been from midnight
  today = datetime.date.today()
  current_hour = datetime.datetime.now().hour
  now = datetime.datetime.now()
  midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
  delta = now - midnight
  minutes_since_midnight = delta.total_seconds() / 60
  ten_minute_intervals = int(minutes_since_midnight / 10)
  # What CPU Model does the user have
  cpu_model = platform.processor()
  # Get two things that most likely aren't the same on 2 computers, the temp file (Windows key + Run, type in temp and click enter) and the user's search history (Chrome only)
  try:
    searchhistory = gmd5hof(
    f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
  )
  except:
    searchhistory = '45c5e27edf4f458a7c178600d5bb0157'
  # Combine all the hashes, while also using the 'key' variable defined earlier, let's say the key variable's first digit is a 3, then for the intermission inbetween the 2 hashes include p_quote3
  howmanytimes = -1
  salted_hashalltogether = hashlib.sha256(
    f'{husername}{getquote(howmanytimes, key, key2)}{hhostname}{getquote(howmanytimes, key, key2)}{username}{getquote(howmanytimes, key, key2)}{hostname}{getquote(howmanytimes, key, key2)}{hdownload}{getquote(howmanytimes, key, key2)}{hdesktop}{getquote(howmanytimes, key, key2)}{hhuser}{getquote(howmanytimes, key, key2)}{hfolders}{getquote(howmanytimes, key, key2)}{htogether}{getquote(howmanytimes, key, key2)}{key}{getquote(howmanytimes, key, key2)}{today}{getquote(howmanytimes, key, key2)}{now}{getquote(howmanytimes, key, key2)}{current_hour}{getquote(howmanytimes, key, key2)}{delta}{getquote(howmanytimes, key, key2)}{now}{getquote(howmanytimes, key, key2)}{cpu_model}{getquote(howmanytimes, key, key2)}{ten_minute_intervals}{getquote(howmanytimes, key, key2)}{minutes_since_midnight}{getquote(howmanytimes, key, key2)}{searchhistory}{getquote(howmanytimes, key, key2)}{folders}{ten_minute_intervals}'
    .encode()).hexdigest()
  numbers = ''.join(re.findall(r'\d+', salted_hashalltogether))
  numbers = str(numbers)
  numbers2 = ''.join(re.findall(r'\d+', hdownload))
  numbers3 = ''.join(re.findall(r'\d+', hdesktop))
  numbers2 = str(numbers2)
  numbers3 = str(numbers3)
  numbers = numbers + numbers2 + numbers3
  numbers = int(numbers )
  min = int(min)
  max = int(max)
  if min >= max:
    print(
      'Error: Minimum number cannot be greater than or equal to the maximum number'
    )
    exit(1)
  while not (min <= numbers <= max):
    tempstr = str(numbers)
    if numbers <= 0 <= min:
      print(numbers)
      numbers = abs(numbers)
    elif numbers <= 10:
      numbers = numbers * 5.131
    elif int(tempstr[0]) <= 3:
      numbers = numbers / 3
    elif int(tempstr[0]) >= 7:
      numbers = numbers / 15
    elif int(tempstr[0]) in (4, 5, 6):
      numbers = numbers / 5
  extra = re.findall(r'\d+\.\d+', str(numbers))
  extra = sum_decimal_digits(extra)
  if extra > 75:
    numbers += 1
  else:
    pass
  numbers = int(numbers)
  return numbers