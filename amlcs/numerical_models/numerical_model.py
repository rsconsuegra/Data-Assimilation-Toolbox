import os


class NumericalModel:
    def __init__(self, model_resolution: dict, variables_by_layers:dict) -> None:
        self.model_resolution:dict = model_resolution
        self.vars_by_layers:dict = variables_by_layers
    
    def set_time_integration(self, times:list[int]) -> None:
        nmonths = times[0]
        days = times[1]
        restart = times[2]
        return nmonths,days,restart
        #self.create_cls_instep_file(nmonths, days, restart)
        #self.create_cls_indyns_file()
        #os.system(f"mv cls_instep.h {self.nmonths}cls_instep.h; mv cls_indyns.h {self.source_local}cls_indyns.h; cd {self.source_local}/ ; sh compile.sh>out.txt;")