def cleanStats(frame):
        frame1 = frame
        fgm = []
        fga = []
        threePTm = []
        threePTa = []
        ftm = []
        fta = []
        fg = frame1['FG'].tolist()
        threePT = frame1['3PT'].tolist()
        ft = frame1["FT"].tolist()
        listLen1 = len(fg)
        listLen2 = len(threePT)
        listLen3 = len(ft)
        for x in range(listLen1):
            fg1 = fg[x]
            out = fg1.split("-")
            out1 = out[0]
            out2 = out[1]
            fgm.append(out1)
            fga.append(out2)

        for x in range(listLen2):
            threePT1 = threePT[x]
            out = threePT1.split("-")
            out1 = out[0]
            out2 = out[1]
            threePTm.append(out1)
            threePTa.append(out2)

        for x in range(listLen3):
            ft1 = ft[x]
            out = ft1.split("-")
            out1 = out[0]
            out2 = out[1]
            ftm.append(out1)
            fta.append(out2)

        frame1.insert(1,'FGM',fgm)
        frame1.insert(2,'FGA',fga)
        frame1.drop('FG',inplace=True,axis=1)
        frame1.insert(4,'3PTM',threePTm)
        frame1.insert(5,'3PTA',threePTa)
        frame1.drop('3PT',inplace=True,axis=1)
        frame1.insert(7,'FTM',ftm)
        frame1.insert(8,'FTA',fta)
        frame1.drop('FT',inplace=True,axis=1)
