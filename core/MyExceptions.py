#!/usr/bin/env python3
# encoding: UTF-8

"""
    This file is part of IPGeoLocation tool.
    Copyright (C) 2015-2016 @maldevel
    Modify    (M) 2020-2021 @Hackermachan
    https://github.com/Hackermachan2/IPGeoLocation
    
    IPGeoLocation - Retrieve IP Geolocation information 
    Powered by http://ip-api.com
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.
"""

__author__ = 'HACKERMACHAN'


class UserAgentFileEmptyError(Exception):
    pass

class InvalidTargetError(Exception):
    pass

class TargetsFileEmptyError(Exception):
    pass

class TargetsFileNotSpecifiedError(Exception):
    pass

class UserAgentFileNotSpecifiedError(Exception):
    pass

class ProxyServerNotReachableError(Exception):
    pass

class ProxiesFileNotSpecifiedError(Exception):
    pass

class ProxiesFileEmptyError(Exception):
    pass

class InvalidProxyUrlError(Exception):
    pass
