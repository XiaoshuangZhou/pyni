#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  daqmx.py
#  
#  Copyright 2021 xizhou <xizhou@AARONX1>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.


import nidaqmx

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan('PXI1Slot2/ai0')
    print (task.read())
    print ('Done with 1st reading')

with nidaqmx.Task() as task:
    task.ai_channels.add_ai_voltage_chan('PXI1Slot2/ai0')
    print (task.read(number_of_samples_per_channel = 2))
    


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
