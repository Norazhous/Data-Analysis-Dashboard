
const dataStore = {
    state: () => ({
        //measured data 
        measuredTime: 0,
        T1: 0,
        T2: 0,
        T3: 0,
        T4: 0,
        T5: 0,
        P1: 0,
        P2: 0,
        P3: 0,
        F: 0,
        E: 0,
        ASP: 0,

        //calculated data
        H1: 0,
        H2: 0,
        H3: 0,
        H4: 0,
        H5: 0,
        m: 0,
        QL: 0,
        QH: 0,
        W: 0,
        COP: 0,
        n: 0,
    }),
    mutations: {
        //set the measured parameters value according to the student input
        SETMeasuredTime(state, value) {
            state.measuredTime = value;
        },
        SETT1(state, value) {
            state.T1 = value;
        },
        SETT2(state, value) {
            state.T2 = value;
        },
        SETT3(state, value) {
            state.T3 = value;
        },
        SETT4(state, value) {
            state.T4 = value;
        },
        SETT5(state, value) {
            state.T5 = value;
        },
        SETP1(state, value) {
            state.P1 = value;
        },
        SETP2(state, value) {
            state.P2 = value;
        },
        SETP3(state, value) {
            state.P3 = value;
        },
        SETE(state, value) {
            state.E = value;
        },
        SETF(state, value) {
            state.F = value;
        },
        SETASP(state, value) {
            state.ASP = value;
        },

        //set the calculation data from students input
        SETH1(state, value) {
            state.H1 = value;
        },
        SETH2(state, value) {
            state.H2 = value;
        },
        SETH3(state, value) {
            state.H3 = value;
        },
        SETH4(state, value) {
            state.H4 = value;
        },
        SETH5(state, value) {
            state.H5 = value;
        },
        SETm(state, value) {
            state.m = value;
        },
        SETQL(state, value) {
            state.QL = value;
        },
        SETQH(state, value) {
            state.QH = value;
        },
        SETW(state, value) {
            state.W = value;
        },
        SETCOP(state, value) {
            state.COP = value;
        },
        SETn(state, value) {
            state.n = value;
        },
    },
    actions: {
        //commit the mutation of setting value of measured data 
        SetMeasuredTime(context, value) {
            context.commit('SETMeasuredTime', value);
        },
        SetT1(context, value) {
            context.commit('SETT1', value)
        },
        SetT2(context, value) {
            context.commit('SETT2', value)
        },
        SetT3(context, value) {
            context.commit('SETT3', value)
        },
        SetT4(context, value) {
            context.commit('SETT4', value)
        },
        SetT5(context, value) {
            context.commit('SETT5', value)
        },
        SetP1(context, value) {
            context.commit('SETP1', value)
        },
        SetP2(context, value) {
            context.commit('SETP2', value)
        },
        SetP3(context, value) {
            context.commit('SETP3', value)
        },
        SetE(context, value) {
            context.commit('SETE', value)
        },
        SetF(context, value) {
            context.commit('SETF', value)
        },
        SetASP(context, value) {
            context.commit('SETASP', value)
        },

        //commit the mutation of setting value of students calculation 
        SetH1(context, value) {
            context.commit('SETH1 ', value)
        },
        SetH2(context, value) {
            context.commit('SETH2 ', value)
        },
        SetH3(context, value) {
            context.commit('SETH3 ', value)
        },
        SetH4(context, value) {
            context.commit('SETH4 ', value)
        },
        SetH5(context, value) {
            context.commit('SETH5 ', value)
        },
        Setm(context, value) {
            context.commit('SETm  ', value)
        },
        SetQL(context, value) {
            context.commit('SETQL ', value)
        },
        SetQH(context, value) {
            context.commit('SETQH ', value)
        },
        SetW(context, value) {
            context.commit('SETW  ', value)
        },
        SetCO(context, value) {
            context.commit('SETCOP', value)
        },
        Setn(context, value) {
            context.commit('SETn  ', value)
        },

    },
    getters: {

        // get the measured data
        GetMeasuredTime(state) {
            return state.measuredTime
        },
        GetT1(state) {
            return state.T1
        },
        GetT2(state) {
            return state.T2
        },
        GetT3(state) {
            return state.T3
        },
        GetT4(state) {
            return state.T4
        },
        GetT5(state) {
            return state.T5
        },
        GetP1(state) {
            return state.P1
        },
        GetP2(state) {
            return state.P2
        },
        GetP3(state) {
            return state.P3
        },
        GetE(state) {
            return state.E
        },
        GetF(state) {
            return state.F
        },
        GetASP(state) {
            return state.ASP
        },

        //get students calcuation data 
        GetH1(state) {
            return state.H1
        },
        GetH2(state) {
            return state.H2
        },
        GetH3(state) {
            return state.H3
        },
        GetH4(state) {
            return state.H4
        },
        GetH5(state) {
            return state.H5
        },
        Getm(state) {
            return state.m
        },
        GetQL(state) {
            return state.QL
        },
        GetQH(state) {
            return state.QH
        },
        GetW(state) {
            return state.W
        },
        GetCOP(state) {
            return state.COP
        },
        Getn(state) {
            return state.n
        },

    },

}

export default dataStore;
