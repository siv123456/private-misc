from distutils.core import setup
import py2exe
 # 'Wb_Restart.pyw', 'Wb_BackupSetup.pyw',
setup(
        windows=[{'script': 'main.pyw'}],
        options={"py2exe":{'optimize':2, 'includes':["sip","decimal"]}
                 }
)

