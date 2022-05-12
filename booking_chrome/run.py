from booking.booking import Booking

with Booking(gg=False) as bot:
    bot.land_first_page()
    bot.change_currency('CNY')
    bot.select_to_go('New York')
    bot.select_date("2022-06-17", "2022-06-18")
    bot.selectAdults(1)
    bot.clickSearch()
    bot.apply_filtrations()
    # a workaround to let our bot to grab the data properly
    bot.refresh()
    bot.report_results()

    print(" exiting ...")
# context manager

# once Python reaches

# the line outside of the indentation

# then it is going to execute
# some tear down actions
