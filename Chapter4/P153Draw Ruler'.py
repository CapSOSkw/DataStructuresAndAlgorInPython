def drawLine(tickLength, tickLabel=""):
    '''
    :param tickLength: int
    :param tickLabel: str
    :return: None

    For example,
    drawLine(3, '1') will print "--- 1"
    drawLine(3, '2') will print "--- 2"

    '''
    line = "-" * tickLength
    if tickLabel:
        line += " " + tickLabel
    print(line)

def drawInterval(center_length):
    '''
    Recursion Trace is illustrated at page154.
    :param center_length: int
    :return: None
    For example,
    drawInterval(3) will print

    -
    --
    -
    ---
    -
    --
    -

    '''
    if center_length > 0:
        drawInterval(center_length - 1)
        drawLine(center_length)
        drawInterval(center_length - 1)

def drawRuler(num_inches, major_length):
    drawLine(major_length, '0')

    for i in range(1, 1+num_inches):
        drawInterval(major_length -1)
        drawLine(major_length, str(i))

if __name__ == '__main__':
    drawRuler(2, 2)