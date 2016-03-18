# coding=UTF8
# Строчка выше нужна на случай использования Non-ASCII символов, например кириллицы.

# Корректирующий множитель для таймаута SNMP-операций. Чем медленнее CPU устройства, тем больше должен быть множитель.
# Этот параметр используется (если задан) для swtoolz-core. Остальные параметры целиком определяются пользователем.
timeout_mf = 1.2

# Карта портов устройства. Преставлена в виде списков слотов. Каждый слот содержит список рядов. Каждый ряд содержит список портов.
DeviceMap = ([
    [
	['1/1','1/3','1/5','1/7','1/9', '1/11','1/13','1/15','1/17','1/19','1/21','1/23','1/25','1/27'],
	['1/2','1/4','1/6','1/8','1/10','1/12','1/14','1/16','1/18','1/20','1/22','1/24','1/26','1/28']
    ],
    [
	['2/1','2/3','2/5','2/7','2/9', '2/11','2/13','2/15','2/17','2/19','2/21','2/23','2/25','2/27'],
	['2/2','2/4','2/6','2/8','2/10','2/12','2/14','2/16','2/18','2/20','2/22','2/24','2/26','2/28']
    ],
    ],)

# SlotSize - количество индексов, отведенное на слот. Обычно это 64, то есть слот №1 - 1..64, слот №2 - 65..128, слот №3 - 129..192 и так далее.
# ShiftIndex - смещение, которое нужно прибавить к индексу. У некоторых устройств первый индекс может начинаться, например, с 256.
# MaxIndex - Максимальный индекс, который нужно обработать. Индексы с большими номерами игнорируются.
# Stackable - поддерживает ли устройство стекирование.
# Chassis - является ли устройство модульным шасси.
# ComboDefMedType - тип среды передачи по умолчанию для комбо-порта.
StackInfo = ({
    'SlotSize'        : '64',
    'ShiftIndex'      : '0',
#    'MaxIndex'        : '64',
    'Stackable'       : 'True',
    'Chassis'         : 'False',
    'ComboDefMedType' : 'fiber',
    },)

# Список рекомендуемых команд
Commands = ([
    'StackInfo',
    'MediumType',
    'ActualStatus',
    'ActualSpeed',
    'AdminStatus',
    'AdminSpeed',
    'AdminFlow',
    'BoardDescrShort',
    'walk_PortIndex',
    'walk_BoardDescr',
    'get_HardwareRev',
    ],)

# swL2PortInfoMediumType
MediumType = ({
    '1' : 'copper',
    '2' : 'fiber',
    },)

# swL2PortInfoLinkStatus
ActualStatus = ({
    '1' : 'other',
    '2' : 'linkup',
    '3' : 'linkdown',
    },)

# swL2PortInfoNwayStatus
ActualSpeed = ({
    '0'  : 'linkdown',
    '1'  : '10M-Full-8023x',
    '2'  : '10M-Full',
    '3'  : '10M-Half-backp',
    '4'  : '10M-Half',
    '5'  : '100M-Full-8023x',
    '6'  : '100M-Full',
    '7'  : '100M-Half-backp',
    '8'  : '100M-Half',
    '9'  : '1G-Full-8023x',
    '10' : '1G-Full',
    '11' : '1G-Half-backp',
    '12' : '1G-Half',
    '13' : '10G-Full-8023x',
    '14' : '10G-Full',
    '15' : '10G-Half-8023x',
    '16' : '10G-Half',
    '17' : 'empty',
    '18' : 'err-disabled',
    },)

# swL2PortCtrlAdminState
AdminStatus = ({
    '2' : 'disabled',
    '3' : 'enabled',
    },)

# swL2PortCtrlNwayState
AdminSpeed = ({
    '2' : 'auto',
    '3' : '10M-Half',
    '4' : '10M-Full',
    '5' : '100M-Half',
    '6' : '100M-Full',
    '7' : '1G-Half',
    '8' : '1G-Full',
    '9' : '1G-Full-master',
    '10': '1G-Full-slave',
    },)

# swL2PortCtrlFlowCtrlState
AdminFlow = ({
    '1' : 'other',
    '2' : 'disabled',
    '3' : 'enabled',
    },)

BoardDescrShort = ({
    'NOT_EXIST' : '',
    },)

get_HardwareRev = {
#    HardwareRev         .1.3.6.1.2.1.16.19.3.0				probeHardwareRev
    'HardwareRev.'    : '.1.3.6.1.2.1.16.19.3.0',
    }

walk_PortIndex = {
#    PortIndex           .1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1		swL2PortInfoPortIndex
    'PortIndex'       : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1',
    }

walk_BoardDescr = {
#    BoardBescr          .1.3.6.1.4.1.171.12.11.1.9.4.1.9		swUnitMgmtModuleName
    'BoardDescr'      : '.1.3.6.1.4.1.171.12.11.1.9.4.1.9',
    }

get_PortIndex = {
#    PortIndex           .1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1		swL2PortInfoPortIndex
    'PortIndex..1'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.1.2',
    'PortIndex..2'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.2.2',
    'PortIndex..3'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.3.2',
    'PortIndex..4'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.4.2',
    'PortIndex..5'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.5.2',
    'PortIndex..6'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.6.2',
    'PortIndex..7'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.7.2',
    'PortIndex..8'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.8.2',
    'PortIndex..9'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.9.2',
    'PortIndex..10'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.10.2',
    'PortIndex..11'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.11.2',
    'PortIndex..12'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.12.2',
    'PortIndex..13'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.13.2',
    'PortIndex..14'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.14.2',
    'PortIndex..15'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.15.2',
    'PortIndex..16'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.16.2',
    'PortIndex..17'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.17.2',
    'PortIndex..18'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.18.2',
    'PortIndex..19'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.19.2',
    'PortIndex..20'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.20.2',
    'PortIndex..21c'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.21.1',
    'PortIndex..21f'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.21.2',
    'PortIndex..22c'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.22.1',
    'PortIndex..22f'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.22.2',
    'PortIndex..23c'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.23.1',
    'PortIndex..23f'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.23.2',
    'PortIndex..24c'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.24.1',
    'PortIndex..24f'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.24.2',
    'PortIndex..25'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.25.2',
    'PortIndex..26'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.26.2',
    'PortIndex..27'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.27.2',
    'PortIndex..28'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.1.28.2',
    }

get_SinglePort = {
#    MediumType          .1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.2		swL2PortInfoMediumType
    'MediumType..c'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.2.%s.1',
    'MediumType..f'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.2.%s.2',
#    ActualStatus        .1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.5		swL2PortInfoLinkStatus
    'ActualStatus..c' : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.5.%s.1',
    'ActualStatus..f' : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.5.%s.2',
#    ActualSpeed         .1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.6		swL2PortInfoNwayStatus
    'ActualSpeed..c'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.6.%s.1',
    'ActualSpeed..f'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.6.%s.2',
#    AdminStatus         .1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.4		swL2PortCtrlAdminState
    'AdminStatus..c'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.4.%s.1',
    'AdminStatus..f'  : '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.4.%s.2',
#    AdminSpeed          .1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.5		swL2PortCtrlNwayState
    'AdminSpeed..c'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.5.%s.1',
    'AdminSpeed..f'   : '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.5.%s.2',
#    AdminFlow           .1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.6		swL2PortCtrlFlowCtrlState
    'AdminFlow..c'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.6.%s.1',
    'AdminFlow..f'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.6.%s.2',
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr.'      : '.1.3.6.1.2.1.31.1.1.1.18.%s',
#    PortType            .1.3.6.1.4.1.171.12.58.1.1.1.2			swEtherCableDiagPortType
    'PortType.'       : '.1.3.6.1.4.1.171.12.58.1.1.1.2.%s',
    }

walk_AllPorts = {
#    MediumType          .1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.2		swL2PortInfoMediumType
    'MediumType'      : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.2',
#    ActualStatus        .1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.5		swL2PortInfoLinkStatus
    'ActualStatus'    : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.5',
#    ActualSpeed         .1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.6		swL2PortInfoNwayStatus
    'ActualSpeed'     : '.1.3.6.1.4.1.171.11.133.5.1.2.3.1.1.6',
#    AdminStatus         .1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.4		swL2PortCtrlAdminState
    'AdminStatus'     : '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.4',
#    AdminSpeed          .1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.5		swL2PortCtrlNwayState
    'AdminSpeed'      : '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.5',
#    AdminFlow           .1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.6		swL2PortCtrlFlowCtrlState
    'AdminFlow'       : '.1.3.6.1.4.1.171.11.133.5.1.2.3.2.1.6',
    }

walk_ifAlias = {
#    PortDescr           .1.3.6.1.2.1.31.1.1.1.18			ifAlias
    'PortDescr'       : '.1.3.6.1.2.1.31.1.1.1.18',
    }

walk_FDB_VLAN = {
#    FDB                 .1.3.6.1.2.1.17.7.1.2.2.1.2			dot1qTpFdbPort
    'FDB'             : '.1.3.6.1.2.1.17.7.1.2.2.1.2.%s',
    }

walk_VlanEgressPorts = {
#    VEP                 .1.3.6.1.2.1.17.7.1.4.3.1.2			dot1qVlanStaticEgressPorts
    'VEP'             : '.1.3.6.1.2.1.17.7.1.4.3.1.2',
    }

walk_VlanUntaggedPorts = {
#    VUP                 .1.3.6.1.2.1.17.7.1.4.3.1.4			dot1qVlanStaticUntaggedPorts
    'VUP'             : '.1.3.6.1.2.1.17.7.1.4.3.1.4',
    }

set_SaveConfig = [
#     .1.3.6.1.4.1.171.12.1.2.18.4					agentBscFileSystemSaveCfg
    ['.1.3.6.1.4.1.171.12.1.2.18.4', '0', '2', 'INTEGER'],
    ]