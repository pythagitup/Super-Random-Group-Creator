from ClassPeriod import ClassPeriod

def populate_lists(self,period,wanted_groups,widget_list,rand=False):
    for widget in widget_list:
        widget.clear()
    x = ClassPeriod()
    x.set_period(period)
    x.set_roster()
    if rand:
        x.randomize()
    y = x.groups(wanted_groups)
    for i in range(len(widget_list)):
        for j in range(len(y[i])):
            widget_list[i].insertItem(j,y[i][j])
