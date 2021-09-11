"""Exam Python M2

Create Python UI application that will:
* retrieve timezones from this link: (50p)
  * http://worldtimeapi.org/api/timezone
* Allow the user to select a timezone and open a new window indicating the time in the selected timezone using this link: (50p)
  *  http://worldtimeapi.org/api/timezone/<area>/<zone>
Detailed description:
  - all windows must have title (5p)
  - all modules classes and methods must be documented (10p)
  - type hints should be used whenever possible (5p)
  - at least two unittests created for at lest one function (20p)
  - all timezones are displayed. (30p)
  - each timezone clicked will open a new window and show time in that timezone (20p)
  - retrieving time to display is done async or in separate thread or process (10p)

Note: You can choose to pack new Frame or open new window for each displayed time.
For new window you can use tkinter.TopLevel(main_window)"""
import asyncio
import tkinter
import aiohttp
import json
from functools import partial

main_window = tkinter.Tk()
main_window.title("Timezones")


async def time_getter():
    """func doc"""
    async with aiohttp.ClientSession() as session:
        response = await session.request(method='GET', url=f"http://worldtimeapi.org/api/timezone")
        my_time = await response.text()
        return json.loads(my_time)


class TimeZones():
    """class doc"""
    def __init__(self, main_window):
        """method doc"""
        self.root_window = main_window
        self.timezones = self.row_and_col(0,0)

    def row_and_col(self,nr:int,j:int):
        """method doc"""
        x=asyncio.run(time_getter())
        for i in x:
            command = partial(self.func, i)
            self.button = tkinter.Button(self.root_window, text=i, command=command)
            if nr < 40:
                self.button.grid(row=nr, column=j)
                nr = nr + 1
            else:
                nr = 0
                j = j + 1
                self.button.grid(row=nr, column=j)
        return x

    def func(self,location:str):
        """method doc"""
        info=asyncio.run(self.get_time(location))["datetime"][11:19]
        scnd_window=tkinter.Toplevel(main_window)
        scnd_window.title("Time")

        label=tkinter.Label(scnd_window,text=info)
        label.grid(row=0,column=0)

        scnd_window.mainloop()



    async def get_time(self, location:str):
        """method doc"""
        async with aiohttp.ClientSession() as session:
            response = await session.request(method='GET', url=f"http://worldtimeapi.org/api/timezone/{location}")
            my_time = await response.text()
            return json.loads(my_time)

    def run(self):
        """method doc"""
        self.root_window.mainloop()

if __name__=="__main__":
    timezones = TimeZones(main_window)
    timezones.run()

