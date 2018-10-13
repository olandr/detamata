#import networkx as nx
# Schedule has the form: schedule[dayAsInteger (0-4)][dateYYYYMMDD][event (scheduled things)]

schedule = [

	{
		'2018-10-08':
        {'starttime': '08:00', 'endtime': '10:00',
        'starttime': '10:00', 'endtime': '12:00',
        'starttime': '15:00', 'endtime': '17:00',
        }
	},
	{
		'2018-10-09':
        {'starttime': '08:00', 'endtime': '10:00',
         'starttime': '13:00', 'endtime': '15:00'
        }
	},
	{
		'2018-10-10':
        {'starttime': '10:00', 'endtime': '12:00',
        'starttime': '15:00', 'endtime': '17:00',
        'starttime': '17:00', 'endtime': '20:00'
        }
	},
	{
		'2018-10-11':
        {'starttime': '16:00', 'endtime': '18:00',
		'starttime': '10:00', 'endtime': '12:00',
		'starttime': '13:00', 'endtime': '15:00'
        }
    },
	{
        '2018-10-12':
        {'starttime': '08:00', 'endtime': '09:00',
        'starttime': '09:00', 'endtime': '10:00',
        'starttime': '10:00', 'endtime': '12:00'
        }
	}
]


print(schedule[0])
