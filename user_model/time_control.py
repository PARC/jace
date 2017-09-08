import arrow


utc = arrow.utcnow()
local = utc.to("US/Hawaii")
time = arrow.get("2017-09-12T03:00:00.865001-10:00")

print(time.humanize())


currTime = utc.to("US/Pacific")
print(currTime.format("HH"))
print(time.format("HH:mm"))


if time.format("HH:mm") == "03:00":
    print("Hello")

