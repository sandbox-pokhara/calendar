normal_day = """<span>{day}</span>"""
red_day = """<span style="color:red">{day}</span>"""
blank_day = """&nbsp;"""

month_template = """
<div class="item" id="{year}-{month}" style="margin-bottom:50px"">
    <div class="calendar">
        <table>
            <thead>
                <tr>
                    <th colspan="7">
                        <div class="title">
                            <span class="mName-{mName}">{mName}</span>
                            <span class="year-{year}">{year}</span>
                            <span class="month-{month}" style="display:none">{month}</span>
                        </div>
                    </th>
                </tr>
            </thead>
            <tr>
                <th>Sun</th>
                <th>Mon</th>
                <th>Tue</th>
                <th>Wed</th>
                <th>Thu</th>
                <th>Fri</th>
                <th>Sat</th>
            </tr>
            <tbody style="text-align:center;">
                <tr>
                    <td class="box-1" id="box-{year}-{month}-{days_int[1]}">{days[1]}</td>
                    <td class="box-2" id="box-{year}-{month}-{days_int[2]}">{days[2]}</td>
                    <td class="box-3" id="box-{year}-{month}-{days_int[3]}">{days[3]}</td>
                    <td class="box-4" id="box-{year}-{month}-{days_int[4]}">{days[4]}</td>
                    <td class="box-5" id="box-{year}-{month}-{days_int[5]}">{days[5]}</td>
                    <td class="box-6" id="box-{year}-{month}-{days_int[6]}">{days[6]}</td>
                    <td class="box-7" id="box-{year}-{month}-{days_int[7]}">{days[7]}</td>
                </tr>
                <tr>
                    <td class="box-8" id="box-{year}-{month}-{days_int[8]}">{days[8]}</td>
                    <td class="box-9" id="box-{year}-{month}-{days_int[9]}">{days[9]}</td>
                    <td class="box-10" id="box-{year}-{month}-{days_int[10]}">{days[10]}</td>
                    <td class="box-11" id="box-{year}-{month}-{days_int[11]}">{days[11]}</td>
                    <td class="box-12" id="box-{year}-{month}-{days_int[12]}">{days[12]}</td>
                    <td class="box-13" id="box-{year}-{month}-{days_int[13]}">{days[13]}</td>
                    <td class="box-14" id="box-{year}-{month}-{days_int[14]}">{days[14]}</td>
                </tr>
                <tr>
                    <td class="box-15" id="box-{year}-{month}-{days_int[15]}">{days[15]}</td>
                    <td class="box-16" id="box-{year}-{month}-{days_int[16]}">{days[16]}</td>
                    <td class="box-17" id="box-{year}-{month}-{days_int[17]}">{days[17]}</td>
                    <td class="box-18" id="box-{year}-{month}-{days_int[18]}">{days[18]}</td>
                    <td class="box-19" id="box-{year}-{month}-{days_int[19]}">{days[19]}</td>
                    <td class="box-20" id="box-{year}-{month}-{days_int[20]}">{days[20]}</td>
                    <td class="box-21" id="box-{year}-{month}-{days_int[21]}">{days[21]}</td>
                </tr>
                <tr>
                    <td class="box-22" id="box-{year}-{month}-{days_int[22]}">{days[22]}</td>
                    <td class="box-23" id="box-{year}-{month}-{days_int[23]}">{days[23]}</td>
                    <td class="box-24" id="box-{year}-{month}-{days_int[24]}">{days[24]}</td>
                    <td class="box-25" id="box-{year}-{month}-{days_int[25]}">{days[25]}</td>
                    <td class="box-26" id="box-{year}-{month}-{days_int[26]}">{days[26]}</td>
                    <td class="box-27" id="box-{year}-{month}-{days_int[27]}">{days[27]}</td>
                    <td class="box-28" id="box-{year}-{month}-{days_int[28]}">{days[28]}</td>
                </tr>
                <tr>
                    <td class="box-29" id="box-{year}-{month}-{days_int[29]}">{days[29]}</td>
                    <td class="box-30" id="box-{year}-{month}-{days_int[30]}">{days[30]}</td>
                    <td class="box-31" id="box-{year}-{month}-{days_int[31]}">{days[31]}</td>
                    <td class="box-32" id="box-{year}-{month}-{days_int[32]}">{days[32]}</td>
                    <td class="box-33" id="box-{year}-{month}-{days_int[33]}">{days[33]}</td>
                    <td class="box-34" id="box-{year}-{month}-{days_int[34]}">{days[34]}</td>
                    <td class="box-35" id="box-{year}-{month}-{days_int[35]}">{days[35]}</td>
                </tr>
            </tbody>
        </table>
    </div>
    <div class="holidays">
        <p>{holidays_str}</p>
    </div>
</div>
"""
