import { configureStore, createSlice, PayloadAction } from '@reduxjs/toolkit'
import { useDispatch, useSelector } from 'react-redux'

interface DashboardState {
  data: any
  loading: boolean
  error: string | null
}

const dashboardSlice = createSlice({
  name: 'dashboard',
  initialState: {
    data: null,
    loading: false,
    error: null,
  } as DashboardState,
  reducers: {
    setDashboardData: (state, action: PayloadAction<any>) => {
      state.data = action.payload
      state.error = null
    },
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.loading = action.payload
    },
    setError: (state, action: PayloadAction<string>) => {
      state.error = action.payload
    },
  },
})

export const store = configureStore({
  reducer: {
    dashboard: dashboardSlice.reducer,
  },
})

export const { setDashboardData, setLoading, setError } = dashboardSlice.actions
export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch

export const useAppDispatch = () => useDispatch<AppDispatch>()
export const useAppSelector = useSelector as <T,>(selector: (state: RootState) => T) => T
